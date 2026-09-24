import express from "express";
import { spawn, execSync, ChildProcess } from "child_process";
import http from "http";
import fs from "fs";
import path from "path";
import { createProxyMiddleware } from "http-proxy-middleware";

// Resolve listening port from command line arguments or environment variable
const args = process.argv.slice(2);
let resolvedPort = 3000;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--port" && args[i + 1]) {
    const p = parseInt(args[i + 1], 10);
    if (!isNaN(p)) resolvedPort = p;
  }
}
if (process.env.PORT) {
  const p = parseInt(process.env.PORT, 10);
  if (!isNaN(p)) resolvedPort = p;
}

const PORT = resolvedPort;
const FLASK_PORT = 5000;
const FLASK_HOST = "127.0.0.1";

let pythonProcess: ChildProcess | null = null;
let isShuttingDown = false;

function ensurePythonDeps() {
  try {
    execSync("python3 -c 'import flask, PIL, numpy, werkzeug'", { stdio: "ignore" });
  } catch {
    console.log("Missing Python dependencies detected. Bootstrapping packages...");
    try {
      execSync(
        "apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3-flask python3-pil python3-numpy python3-werkzeug",
        { stdio: "inherit" }
      );
      console.log("Python packages bootstrapped successfully.");
    } catch (e: any) {
      console.warn("Python package bootstrap failed:", e?.message);
    }
  }
}

function findPythonExecutable(): string {
  const candidates = [
    path.resolve(process.cwd(), "python_env/bin/python3"),
    path.resolve(process.cwd(), "python_env/bin/python"),
    process.env.PYTHON_PATH,
    "/usr/bin/python3",
    "/usr/local/bin/python3",
    "python3",
    "python"
  ].filter(Boolean) as string[];

  for (const candidate of candidates) {
    if (candidate.startsWith("/") || candidate.startsWith(".")) {
      if (fs.existsSync(candidate)) {
        return candidate;
      }
    } else {
      return candidate;
    }
  }
  return "python3";
}

function startFlaskBackend(): Promise<void> {
  return new Promise((resolve) => {
    ensurePythonDeps();
    const pythonCmd = findPythonExecutable();
    console.log(`Starting PackSense AI Python/Flask backend using "${pythonCmd}" on port ${FLASK_PORT}...`);
    
    try {
      pythonProcess = spawn(pythonCmd, ["-u", "app.py"], {
        env: {
          ...process.env,
          FLASK_PORT: String(FLASK_PORT),
          FLASK_HOST: FLASK_HOST,
          PYTHONUNBUFFERED: "1",
        },
        stdio: ["ignore", "pipe", "pipe"],
      });

      pythonProcess.stdout?.on("data", (data) => {
        process.stdout.write(`[PackSense Flask] ${data}`);
      });

      pythonProcess.stderr?.on("data", (data) => {
        const msg = data.toString();
        if (
          msg.includes("Traceback (most recent call last)") ||
          msg.includes("Error:") ||
          msg.includes("Exception:") ||
          msg.includes("CRITICAL")
        ) {
          process.stderr.write(`[PackSense Flask Error] ${msg}`);
        } else {
          process.stdout.write(`[PackSense Flask] ${msg}`);
        }
      });

      pythonProcess.on("error", (err) => {
        console.error("Warning: Failed to spawn Python process:", err.message);
        resolve();
      });

      pythonProcess.on("exit", (code, signal) => {
        console.warn(`Flask backend exited with code ${code}, signal ${signal}`);
        if (!isShuttingDown) {
          console.log("Attempting automatic Flask restart in 2 seconds...");
          setTimeout(() => {
            if (!isShuttingDown) {
              startFlaskBackend().catch((e) => console.error("Flask restart failed:", e));
            }
          }, 2000);
        }
      });
    } catch (spawnErr) {
      console.error("Exception spawning Python:", spawnErr);
      resolve();
      return;
    }

    // Poll until Flask is ready to accept requests
    const checkInterval = setInterval(() => {
      const req = http.get(`http://${FLASK_HOST}:${FLASK_PORT}/`, (res) => {
        clearInterval(checkInterval);
        clearTimeout(timeout);
        console.log(`PackSense AI Flask backend is online and accepting connections on port ${FLASK_PORT}!`);
        resolve();
      });

      req.on("error", () => {
        // Still warming up, keep polling
      });

      req.end();
    }, 250);

    const timeout = setTimeout(() => {
      clearInterval(checkInterval);
      console.warn("Flask startup healthcheck timed out, proceeding with proxy launch...");
      resolve();
    }, 10000);
  });
}

async function startServer() {
  const app = express();

  // Serve static assets directly from Express for rapid caching & speed
  app.use("/static", express.static(path.resolve(process.cwd(), "static")));
  app.use("/packsense-chatbot", express.static(path.resolve(process.cwd(), "packsense-chatbot")));

  // Start Flask backend asynchronously
  startFlaskBackend().catch((e) => console.error("Flask startup warning:", e));

  // Reverse proxy all HTTP requests to Flask backend with friendly fallback
  app.use(
    "/",
    createProxyMiddleware({
      target: `http://${FLASK_HOST}:${FLASK_PORT}`,
      changeOrigin: true,
      ws: false,
      on: {
        error: (err: any, req: any, res: any) => {
          console.warn(`Proxy request to ${req.url} pending backend readiness (${err.message})`);
          if (!res.headersSent && typeof res.status === "function") {
            res.status(503).send(`
              <!DOCTYPE html>
              <html lang="en">
                <head>
                  <meta charset="UTF-8">
                  <title>PackSense AI - Starting Service</title>
                  <meta http-equiv="refresh" content="2">
                  <style>
                    body {
                      margin: 0;
                      padding: 0;
                      min-height: 100vh;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                      background: #0b1a2d;
                      color: #ffffff;
                      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                      text-align: center;
                    }
                    .card {
                      background: #112843;
                      border: 1px solid #1e3a5f;
                      padding: 2.5rem;
                      border-radius: 16px;
                      max-width: 480px;
                      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                    }
                    .spinner {
                      width: 40px;
                      height: 40px;
                      border: 3px solid rgba(34, 197, 94, 0.2);
                      border-top-color: #22c55e;
                      border-radius: 50%;
                      animation: spin 0.8s linear infinite;
                      margin: 0 auto 1.5rem;
                    }
                    @keyframes spin { to { transform: rotate(360deg); } }
                  </style>
                </head>
                <body>
                  <div class="card">
                    <div class="spinner"></div>
                    <h2 style="margin: 0 0 0.5rem; font-size: 1.5rem; font-weight: 800;">PackSense AI</h2>
                    <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 0;">Initializing AI Engine and Services. This page will connect automatically...</p>
                  </div>
                </body>
              </html>
            `);
          }
        }
      }
    })
  );

  const server = app.listen(PORT, "0.0.0.0", () => {
    console.log(`PackSense AI web application running on http://0.0.0.0:${PORT}`);
  });

  // Graceful shutdown handling
  const shutdown = () => {
    isShuttingDown = true;
    console.log("Shutting down PackSense AI server...");
    server.close();
    if (pythonProcess) {
      pythonProcess.kill("SIGTERM");
    }
    process.exit(0);
  };

  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
}

startServer().catch((err) => {
  console.error("Server startup error:", err);
});
