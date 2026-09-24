"""
PackSense AI - Main Flask Application
Smart Packaging Material Recommendation System for Food Commodities
SIH Problem Statement 236
"""

import os
import json
import sqlite3
import hashlib
import urllib.parse
from datetime import datetime
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, jsonify, flash, send_from_directory, make_response
)
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash

from ai.knowledge_base import (
    get_db_connection, init_db,
    get_all_foods, get_food_by_name, get_all_cities, get_all_materials
)
from ai.translations import SUPPORTED_LANGUAGES, get_translation
from ai.climate_engine import calculate_climate_stress
from ai.packaudit_engine import analyze_packaging_image, get_fallback_packaudit
from ai.recommendation_engine import run_packsense_engine
from chatbot_service import handle_chatbot_query

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "packsense-ai-super-secret-key-2026")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Enable iframe-friendly session cookies
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_PATH"] = "/"

UPLOAD_FOLDER = os.path.join(app.root_path, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def verify_password(stored_hash, raw_pwd):
    """Verifies password using SHA-256, Werkzeug check_password_hash, or direct comparison."""
    if not stored_hash or not raw_pwd:
        return False
    # SHA-256 match
    if stored_hash == hashlib.sha256(raw_pwd.encode()).hexdigest():
        return True
    # Werkzeug check_password_hash
    try:
        if check_password_hash(stored_hash, raw_pwd):
            return True
    except Exception:
        pass
    # Plain text comparison fallback
    if stored_hash == raw_pwd:
        return True
    return False

# -----------------------------------------------------------------------------
# Jinja Context Processors & Language Helpers (All 21 Languages)
# -----------------------------------------------------------------------------
def get_current_lang():
    param_lang = request.args.get("lang")
    if param_lang and param_lang in SUPPORTED_LANGUAGES:
        return param_lang
    if request.form:
        form_lang = request.form.get("lang")
        if form_lang and form_lang in SUPPORTED_LANGUAGES:
            return form_lang
    current = session.get("lang") or request.cookies.get("packsense_lang") or "en"
    return current if current in SUPPORTED_LANGUAGES else "en"

@app.context_processor
def inject_global_utilities():
    current_lang = get_current_lang()
    session["lang"] = current_lang
    
    def t(key):
        return get_translation(key, current_lang)

    # 2. Resilient user detection: session user_id > cookie packsense_user_id
    user_id = session.get("user_id") or request.cookies.get("packsense_user_id")
    user = None
    if user_id:
        try:
            conn = get_db_connection()
            user_row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            conn.close()
            if user_row:
                user = dict(user_row)
                if not user.get("role"):
                    user["role"] = user.get("mode", "farmer")
                if not user.get("mode"):
                    user["mode"] = user.get("role", "farmer")
        except Exception as e:
            print(f"Error fetching user: {e}")

    operating_mode = session.get("operating_mode") or request.cookies.get("packsense_mode") or (user.get("mode") if user else "farmer") or "farmer"
    if user:
        user["mode"] = operating_mode
        user["role"] = operating_mode

    current_lang_info = SUPPORTED_LANGUAGES.get(current_lang, SUPPORTED_LANGUAGES["en"])

    return {
        "t": t,
        "current_user": user,
        "active_lang": current_lang,
        "current_lang_info": current_lang_info,
        "supported_languages": SUPPORTED_LANGUAGES,
        "operating_mode": operating_mode
    }

# -----------------------------------------------------------------------------
# Mode & Language Switchers
# -----------------------------------------------------------------------------
@app.route("/set_mode/<mode>")
def set_mode(mode):
    if mode not in ["farmer", "industry"]:
        mode = "farmer"
    session["operating_mode"] = mode
    user_id = session.get("user_id") or request.cookies.get("packsense_user_id")
    if user_id:
        try:
            conn = get_db_connection()
            conn.execute("UPDATE users SET mode = ?, role = ? WHERE id = ?", (mode, mode, user_id))
            conn.commit()
            conn.close()
        except Exception:
            pass

    next_page = request.args.get("next") or request.referrer or url_for("workspace")
    if not next_page or next_page.startswith("/set_mode"):
        next_page = url_for("workspace")

    resp = make_response(redirect(next_page))
    resp.set_cookie("packsense_mode", mode, max_age=30*86400, path="/", samesite="Lax")
    return resp

@app.route("/set_language/<lang>")
def set_language(lang):
    if lang not in SUPPORTED_LANGUAGES:
        lang = "en"
    session["lang"] = lang

    user_id = session.get("user_id") or request.cookies.get("packsense_user_id")
    if user_id:
        try:
            conn = get_db_connection()
            conn.execute("UPDATE users SET language = ? WHERE id = ?", (lang, user_id))
            conn.commit()
            conn.close()
        except Exception:
            pass

    next_page = request.args.get("next")
    if not next_page or next_page.startswith("/set_language"):
        next_page = url_for("index")

    # Add or update ?lang=<lang> query parameter on the destination URL
    parsed = urllib.parse.urlsplit(next_page)
    qs = urllib.parse.parse_qs(parsed.query)
    qs["lang"] = [lang]
    new_query = urllib.parse.urlencode(qs, doseq=True)
    clean_next = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, new_query, parsed.fragment))

    resp = make_response(redirect(clean_next))
    resp.set_cookie("packsense_lang", lang, max_age=30*86400, path="/", samesite="Lax")
    return resp

# -----------------------------------------------------------------------------
# Home Page
# -----------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# -----------------------------------------------------------------------------
# PackSense AI Workspace
# -----------------------------------------------------------------------------
@app.route("/workspace")
def workspace():
    all_foods = get_all_foods()
    all_cities = get_all_cities()
    
    # Check if a specific food commodity or mode was passed via URL parameter
    preselect_food = request.args.get("food", "Strawberry")
    active_mode = request.args.get("mode", "farmer")
    selected_food = get_food_by_name(preselect_food) or (all_foods[0] if all_foods else None)

    # Optional initial sample audit score passed from PackAudit
    vuln_param = request.args.get("vuln")
    audit_res = None
    if vuln_param:
        audit_res = get_fallback_packaudit(selected_food["name"] if selected_food else "Strawberry", mode=active_mode)
        try:
            audit_res["vulnerability_score"] = int(vuln_param)
        except ValueError:
            pass

    form_data = {
        "condition": "Fresh",
        "storage_duration": 7,
        "storage_type": "Ambient",
        "origin": "Pune",
        "destination": "Chennai",
        "transport_mode": "Ambient Open Truck",
        "transit_days": 4,
        "season": "Monsoon"
    }

    current_lang = get_current_lang()
    # Run default optimization for strawberry on first view so cards are populated
    default_rec = run_packsense_engine(
        food_name=selected_food["name"] if selected_food else "Strawberry",
        condition="Fresh",
        storage_duration=7,
        storage_type="Ambient",
        origin="Pune",
        destination="Chennai",
        transport_mode="Ambient Open Truck",
        transit_days=4,
        season="Monsoon",
        mode=active_mode,
        lang=current_lang
    )

    return render_template(
        "dashboard.html",
        all_foods=all_foods,
        all_cities=all_cities,
        selected_food=selected_food,
        form_data=form_data,
        active_mode=active_mode,
        result=default_rec,
        audit_result=audit_res
    )

@app.route("/run_analysis", methods=["GET", "POST"])
def run_analysis():
    all_foods = get_all_foods()
    all_cities = get_all_cities()

    food_name = request.form.get("food_name", "Strawberry")
    selected_food = get_food_by_name(food_name)
    mode = request.form.get("mode", "farmer")

    condition = request.form.get("condition", "Fresh")
    try:
        storage_duration = int(request.form.get("storage_duration", 7))
    except ValueError:
        storage_duration = 7

    storage_type = request.form.get("storage_type", "Ambient")
    origin = request.form.get("origin", "Pune")
    destination = request.form.get("destination", "Chennai")
    transport_mode = request.form.get("transport_mode", "Ambient Open Truck")
    try:
        transit_days = int(request.form.get("transit_days", 4))
    except ValueError:
        transit_days = 4
    season = request.form.get("season", "Monsoon")

    # Industry / Lab parameters
    def parse_float(val):
        try:
            return float(val) if val else None
        except ValueError:
            return None

    initial_moisture = parse_float(request.form.get("initial_moisture"))
    free_fat = parse_float(request.form.get("free_fat"))
    manual_otr = parse_float(request.form.get("manual_otr"))
    manual_wvtr = parse_float(request.form.get("manual_wvtr"))
    seal_strength = parse_float(request.form.get("seal_strength"))
    film_thickness = parse_float(request.form.get("film_thickness"))

    # Channel B Image Upload handling
    audit_res = None
    if "packaging_image" in request.files:
        file = request.files["packaging_image"]
        if file and file.filename != "" and allowed_file(file.filename):
            filename = secure_filename(f"upload_{int(datetime.now().timestamp())}_{file.filename}")
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)
            audit_res = analyze_packaging_image(save_path, target_food_name=food_name, mode=mode)

    current_lang = get_current_lang()
    # Run the core Multi-Factor Engine
    result = run_packsense_engine(
        food_name=food_name,
        condition=condition,
        storage_duration=storage_duration,
        storage_type=storage_type,
        origin=origin,
        destination=destination,
        transport_mode=transport_mode,
        transit_days=transit_days,
        season=season,
        initial_moisture=initial_moisture,
        free_fat=free_fat,
        manual_otr=manual_otr,
        manual_wvtr=manual_wvtr,
        seal_strength=seal_strength,
        film_thickness=film_thickness,
        mode=mode,
        lang=current_lang
    )

    # Persist record into SQLite Database
    try:
        user_id = session.get("user_id")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO analyses (
                user_id, mode, food_name, condition, storage_duration, storage_type,
                origin, destination, transport_mode, transit_days, season,
                initial_moisture, free_fat
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, mode, food_name, condition, storage_duration, storage_type,
            origin, destination, transport_mode, transit_days, season,
            initial_moisture, free_fat
        ))
        analysis_id = cur.lastrowid

        cur.execute("""
            INSERT INTO recommendations (
                analysis_id, primary_material, material_configuration,
                optimized_gauge, packaging_type, otr_target, wvtr_target,
                map_o2, map_co2, map_n2, bio_alternative_1, bio_alternative_2,
                shelf_life_original, shelf_life_extended, shelf_life_extension_pct,
                sustainability_score, unit_cost_inr, plastic_reduction_pct,
                carbon_impact, climate_stress_score, humidity_risk_score,
                temperature_risk_score, transit_risk_score, smart_insight
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            analysis_id,
            result["primary_material"],
            result["material_configuration"],
            result["optimized_gauge"],
            result["packaging_type"],
            result["otr_target"],
            result["wvtr_target"],
            result["map_o2"],
            result["map_co2"],
            result["map_n2"],
            json.dumps(result["bio_alternative_1"]),
            json.dumps(result["bio_alternative_2"]),
            result["shelf_life_original"],
            result["shelf_life_extended"],
            result["shelf_life_extension_pct"],
            result["sustainability_score"],
            result["unit_cost_inr"],
            result["plastic_reduction_pct"],
            result["carbon_impact"],
            result["climate_stress_score"],
            result["humidity_risk_score"],
            result["temperature_risk_score"],
            result["transit_risk_score"],
            result["smart_insight"]
        ))

        if audit_res:
            cur.execute("""
                INSERT INTO packaudit_results (
                    analysis_id, image_filename, opacity_pct, reflectivity_pct,
                    detected_type, seal_integrity, vulnerability_score,
                    vulnerability_reason, recommended_upgrade
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                analysis_id, "uploaded_sample.jpg",
                audit_res.get("opacity_pct", 50.0),
                audit_res.get("reflectivity_pct", 20.0),
                audit_res.get("detected_type", "Standard Polyolefin Film"),
                audit_res.get("seal_integrity", "Fair"),
                audit_res.get("vulnerability_score", 5),
                audit_res.get("vulnerability_reason", ""),
                audit_res.get("recommended_upgrade", "")
            ))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database write error: {e}")

    form_data = {
        "condition": condition,
        "storage_duration": storage_duration,
        "storage_type": storage_type,
        "origin": origin,
        "destination": destination,
        "transport_mode": transport_mode,
        "transit_days": transit_days,
        "season": season,
        "initial_moisture": initial_moisture,
        "free_fat": free_fat,
        "manual_otr": manual_otr,
        "manual_wvtr": manual_wvtr,
        "seal_strength": seal_strength,
        "film_thickness": film_thickness,
        "mode": mode
    }

    flash("Packaging optimization successfully calibrated!", "success")

    return render_template(
        "dashboard.html",
        all_foods=all_foods,
        all_cities=all_cities,
        selected_food=selected_food,
        form_data=form_data,
        active_mode=mode,
        result=result,
        audit_result=audit_res,
        analysis_id=analysis_id
    )

# -----------------------------------------------------------------------------
# Channel B: Dedicated Visual PackAudit
# -----------------------------------------------------------------------------
@app.route("/packaudit", methods=["GET", "POST"])
def packaudit():
    all_foods = get_all_foods()
    selected_food = request.args.get("food", "Strawberry")
    mode = request.args.get("mode") or request.form.get("mode") or "farmer"
    audit_res = None
    img_url = None

    if request.method == "POST":
        selected_food = request.form.get("food_name", "Strawberry")
        mode = request.form.get("mode", mode)
        if "audit_image" in request.files:
            file = request.files["audit_image"]
            if file and file.filename != "" and allowed_file(file.filename):
                filename = secure_filename(f"audit_{int(datetime.now().timestamp())}_{file.filename}")
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(save_path)
                img_url = url_for("static", filename=f"uploads/{filename}")
                audit_res = analyze_packaging_image(save_path, target_food_name=selected_food, mode=mode)
            else:
                audit_res = get_fallback_packaudit(selected_food, mode=mode)
        else:
            audit_res = get_fallback_packaudit(selected_food, mode=mode)
    else:
        # Initial view: provide baseline sample audit
        audit_res = get_fallback_packaudit(selected_food, mode=mode)

    return render_template(
        "packaudit.html",
        all_foods=all_foods,
        selected_food=selected_food,
        active_mode=mode,
        audit_result=audit_res,
        uploaded_image_url=img_url
    )

# -----------------------------------------------------------------------------
# API: JSON Food Biochemical Attributes
# -----------------------------------------------------------------------------
@app.route("/api/food/<food_name>")
def api_food(food_name):
    food = get_food_by_name(food_name)
    if food:
        return jsonify({"success": True, "food": food})
    return jsonify({"success": False, "error": "Food commodity not found"}), 404

# -----------------------------------------------------------------------------
# History & Full Reports
# -----------------------------------------------------------------------------
@app.route("/history")
def history():
    conn = get_db_connection()
    user_id = session.get("user_id")
    if user_id:
        rows = conn.execute("""
            SELECT a.id, a.food_name, a.condition, a.storage_type, a.storage_duration,
                   a.origin, a.destination, a.transport_mode, a.transit_days, a.season, a.created_at,
                   r.primary_material, r.optimized_gauge, r.packaging_type, r.otr_target, r.wvtr_target,
                   r.shelf_life_original, r.shelf_life_extended, r.shelf_life_extension_pct,
                   r.sustainability_score, r.unit_cost_inr
            FROM analyses a
            JOIN recommendations r ON a.id = r.analysis_id
            WHERE a.user_id = ?
            ORDER BY a.id DESC
        """, (user_id,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT a.id, a.food_name, a.condition, a.storage_type, a.storage_duration,
                   a.origin, a.destination, a.transport_mode, a.transit_days, a.season, a.created_at,
                   r.primary_material, r.optimized_gauge, r.packaging_type, r.otr_target, r.wvtr_target,
                   r.shelf_life_original, r.shelf_life_extended, r.shelf_life_extension_pct,
                   r.sustainability_score, r.unit_cost_inr
            FROM analyses a
            JOIN recommendations r ON a.id = r.analysis_id
            ORDER BY a.id DESC LIMIT 25
        """).fetchall()
    conn.close()

    analyses = [dict(r) for r in rows]
    return render_template("history.html", analyses=analyses)

def enrich_analysis_for_report(row):
    d = dict(row)
    analysis_id = d.get("id") or 1
    d["report_id"] = f"PSA-{680300 + analysis_id if analysis_id < 1000 else analysis_id}"

    # Corridor distance lookup
    city_distances = {
        ("pune", "chennai"): 1143,
        ("chennai", "pune"): 1143,
        ("mumbai", "delhi"): 1420,
        ("delhi", "mumbai"): 1420,
        ("nashik", "mumbai"): 166,
        ("mumbai", "nashik"): 166,
        ("nagpur", "mumbai"): 810,
        ("bengaluru", "chennai"): 346,
        ("hyderabad", "bengaluru"): 575,
        ("kolkata", "delhi"): 1490,
        ("ahmedabad", "mumbai"): 525
    }
    orig = str(d.get("origin", "")).strip().lower()
    dest = str(d.get("destination", "")).strip().lower()
    d["corridor_distance"] = city_distances.get((orig, dest), 1143)

    # Dynamic climate multiplier
    stress = float(d.get("climate_stress_score") or 85)
    mult = round(stress / 54.5, 2)
    if mult < 1.05:
        mult = 1.15
    d["climate_multiplier"] = mult

    # Audit score
    audit_score = round(max(2.0, min(9.5, 10.0 - (stress * 0.078))), 1)
    d["audit_score"] = audit_score
    if audit_score < 4.5:
        d["audit_score_label"] = f"{audit_score} / 10 (Inadequate moisture ventilation & anti-fog protection)"
    elif audit_score < 7.0:
        d["audit_score_label"] = f"{audit_score} / 10 (Moderate baseline barrier; vulnerable to humidity surge)"
    else:
        d["audit_score_label"] = f"{audit_score} / 10 (Acceptable baseline barrier)"

    # Formatted timestamp
    created_at = d.get("created_at")
    if created_at:
        try:
            if isinstance(created_at, str):
                dt = datetime.strptime(created_at[:19], "%Y-%m-%d %H:%M:%S")
            else:
                dt = created_at
            # Format like: 22 Sept 2026, 11:37 pm
            day = dt.strftime("%d").lstrip("0")
            month = dt.strftime("%b")
            year = dt.strftime("%Y")
            time_part = dt.strftime("%I:%M %p").lower()
            d["formatted_date"] = f"{day} {month} {year}, {time_part}"
        except Exception:
            d["formatted_date"] = "22 Sept 2026, 11:37 pm"
    else:
        d["formatted_date"] = "22 Sept 2026, 11:37 pm"

    return d

@app.route("/history/<int:analysis_id>")
def view_recommendation(analysis_id):
    conn = get_db_connection()
    row = conn.execute("""
        SELECT a.id, a.food_name, a.condition, a.storage_type, a.storage_duration,
               a.origin, a.destination, a.transport_mode, a.transit_days, a.season, a.created_at,
               r.primary_material, r.optimized_gauge, r.packaging_type, r.otr_target, r.wvtr_target,
               r.map_o2, r.map_co2, r.map_n2, r.shelf_life_original, r.shelf_life_extended,
               r.shelf_life_extension_pct, r.sustainability_score, r.unit_cost_inr,
               r.plastic_reduction_pct, r.carbon_impact, r.climate_stress_score, r.smart_insight,
               r.bio_alternative_1, r.bio_alternative_2
        FROM analyses a
        JOIN recommendations r ON a.id = r.analysis_id
        WHERE a.id = ?
    """, (analysis_id,)).fetchone()
    conn.close()
    if not row:
        flash("Report not found.", "error")
        return redirect(url_for("history"))
    enriched = enrich_analysis_for_report(row)
    return render_template("recommendation.html", analysis=enriched)

@app.route("/history/<int:analysis_id>/print")
def print_recommendation(analysis_id):
    conn = get_db_connection()
    row = conn.execute("""
        SELECT a.id, a.food_name, a.condition, a.storage_type, a.storage_duration,
               a.origin, a.destination, a.transport_mode, a.transit_days, a.season, a.created_at,
               r.primary_material, r.optimized_gauge, r.packaging_type, r.otr_target, r.wvtr_target,
               r.map_o2, r.map_co2, r.map_n2, r.shelf_life_original, r.shelf_life_extended,
               r.shelf_life_extension_pct, r.sustainability_score, r.unit_cost_inr,
               r.plastic_reduction_pct, r.carbon_impact, r.climate_stress_score, r.smart_insight,
               r.bio_alternative_1, r.bio_alternative_2
        FROM analyses a
        JOIN recommendations r ON a.id = r.analysis_id
        WHERE a.id = ?
    """, (analysis_id,)).fetchone()
    conn.close()
    if not row:
        flash("Report not found.", "error")
        return redirect(url_for("history", lang=get_current_lang()))
    enriched = enrich_analysis_for_report(row)
    return render_template("recommendation.html", analysis=enriched, is_print_view=True)

@app.route("/history/<int:analysis_id>/delete", methods=["GET", "POST"])
def delete_analysis(analysis_id):
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM recommendations WHERE analysis_id = ?", (analysis_id,))
        conn.execute("DELETE FROM analyses WHERE id = ?", (analysis_id,))
        conn.commit()
        flash("Optimization record deleted successfully.", "success")
    except Exception as e:
        flash(f"Error deleting record: {e}", "error")
    finally:
        conn.close()
    next_url = request.args.get("next") or url_for("history", lang=get_current_lang())
    return redirect(next_url)

@app.route("/history/clear", methods=["GET", "POST"])
def clear_history():
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM recommendations")
        conn.execute("DELETE FROM analyses")
        conn.commit()
        flash("All packaging history records cleared successfully.", "success")
    except Exception as e:
        flash(f"Error clearing history: {e}", "error")
    finally:
        conn.close()
    return redirect(url_for("history", lang=get_current_lang()))

# -----------------------------------------------------------------------------
# About & Technical Documentation
# -----------------------------------------------------------------------------
@app.route("/about")
def about():
    return render_template("about.html")

# -----------------------------------------------------------------------------
# Authentication: Login, Register, Profile, Logout
# -----------------------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        pwd = request.form.get("password", "")

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE LOWER(email) = ?", (email,)).fetchone()
        conn.close()

        if user and verify_password(user["password_hash"], pwd):
            session["user_id"] = user["id"]
            if user["language"] and user["language"] in ["en", "hi", "mr"]:
                session["lang"] = user["language"]
            
            flash(f"Welcome back, {user['name']}!", "success")
            
            target = request.args.get("next") or url_for("workspace")
            if target.startswith("/login") or target.startswith("/logout"):
                target = url_for("workspace")
                
            active_lang = session.get("lang") or request.args.get("lang") or "en"
            parsed = urllib.parse.urlsplit(target)
            qs = urllib.parse.parse_qs(parsed.query)
            qs["lang"] = [active_lang]
            new_query = urllib.parse.urlencode(qs, doseq=True)
            clean_target = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, new_query, parsed.fragment))

            resp = make_response(redirect(clean_target))
            resp.set_cookie("packsense_user_id", str(user["id"]), max_age=30*86400, path="/", samesite="None", secure=True)
            resp.set_cookie("packsense_lang", active_lang, max_age=30*86400, path="/", samesite="None", secure=True)
            return resp
        else:
            flash("Invalid email or password. Please try again or use the demo credentials.", "error")

    active_lang = session.get("lang") or request.args.get("lang") or "en"
    return render_template("login.html", active_lang=active_lang)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        role = request.form.get("role", "farmer")
        pwd = request.form.get("password", "")

        if not name or not email or not pwd:
            flash("Please fill in all required registration fields.", "error")
            return render_template("register.html")

        pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

        conn = get_db_connection()
        existing = conn.execute("SELECT id FROM users WHERE LOWER(email) = ?", (email,)).fetchone()
        if existing:
            conn.close()
            flash("An account with this email already exists. Please log in.", "error")
            return redirect(url_for("login"))

        active_lang = session.get("lang") or request.args.get("lang") or "en"
        conn.execute(
            "INSERT INTO users (name, email, password_hash, role, mode, language) VALUES (?, ?, ?, ?, ?, ?)",
            (name, email, pwd_hash, role, role, active_lang)
        )
        conn.commit()
        new_user = conn.execute("SELECT id FROM users WHERE LOWER(email) = ?", (email,)).fetchone()
        conn.close()

        session["user_id"] = new_user["id"]
        flash(f"Account created successfully! Welcome to PackSense AI, {name}.", "success")
        
        target = url_for("workspace", lang=active_lang)
        resp = make_response(redirect(target))
        resp.set_cookie("packsense_user_id", str(new_user["id"]), max_age=30*86400, path="/", samesite="None", secure=True)
        resp.set_cookie("packsense_lang", active_lang, max_age=30*86400, path="/", samesite="None", secure=True)
        return resp

    active_lang = session.get("lang") or request.args.get("lang") or "en"
    return render_template("register.html", active_lang=active_lang)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    user_id = session.get("user_id") or request.cookies.get("packsense_user_id")
    if not user_id:
        flash("Please log in to view your profile.", "error")
        active_lang = session.get("lang") or request.args.get("lang") or "en"
        return redirect(url_for("login", lang=active_lang))

    conn = get_db_connection()
    user_row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    if not user_row:
        conn.close()
        session.pop("user_id", None)
        flash("User profile not found. Please sign in or register.", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        new_name = request.form.get("name", "").strip()
        new_mode = request.form.get("mode", "farmer").strip().lower()
        new_lang = request.form.get("language", "en").strip().lower()
        if new_mode not in ["farmer", "industry"]:
            new_mode = "farmer"

        if new_name:
            conn.execute(
                "UPDATE users SET name = ?, mode = ?, role = ?, language = ? WHERE id = ?",
                (new_name, new_mode, new_mode, new_lang, user_id)
            )
            conn.commit()
            session["lang"] = new_lang
            flash("Profile preferences updated successfully!", "success")
            user_row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

    count_row = conn.execute("SELECT COUNT(*) as count FROM analyses WHERE user_id = ?", (user_id,)).fetchone()
    total_analyses = count_row["count"] if count_row else 0
    conn.close()

    user = dict(user_row) if user_row else None
    return render_template("profile.html", current_user=user, total_analyses=total_analyses)

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been signed out successfully.", "success")
    active_lang = get_current_lang()
    resp = make_response(redirect(url_for("index", lang=active_lang)))
    # Securely wipe authentication cookies across all samesite / secure permutations
    resp.delete_cookie("packsense_user_id", path="/", samesite="None", secure=True)
    resp.set_cookie("packsense_user_id", "", expires=0, max_age=0, path="/", samesite="None", secure=True)
    resp.delete_cookie("packsense_user_id", path="/")
    resp.set_cookie("packsense_user_id", "", expires=0, max_age=0, path="/")
    return resp

# -----------------------------------------------------------------------------
# PackSense AI – Food Safety Assistant Routes
# -----------------------------------------------------------------------------
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/packsense-chatbot/<path:filename>")
def packsense_chatbot_static(filename):
    chatbot_dir = os.path.join(BASE_DIR, "packsense-chatbot")
    return send_from_directory(chatbot_dir, filename)

@app.route("/packsense-chatbot")
@app.route("/packsense-chatbot/")
def packsense_chatbot_root():
    chatbot_dir = os.path.join(BASE_DIR, "packsense-chatbot")
    return send_from_directory(chatbot_dir, "index.html")

@app.route("/api/chatbot/query", methods=["POST"])
def api_chatbot_query():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    history = data.get("history", [])
    if not message:
        return jsonify({"error": "Message cannot be empty", "reply": "Please enter a question regarding food packaging safety or FSSAI regulations."}), 400
    
    reply = handle_chatbot_query(message, history)
    return jsonify({"reply": reply, "status": "success"})

@app.route("/api/chatbot/recommend", methods=["POST"])
def api_chatbot_recommend():
    data = request.get_json(silent=True) or {}
    food_name = data.get("foodName", "Food Item").strip()
    moisture = data.get("moistureLevel", "Moderate")
    fat = data.get("fatContent", "Moderate")
    acidity = data.get("acidity", "Neutral")
    oxygen = data.get("oxygenSensitivity", "Moderate")
    light = data.get("lightSensitivity", "Moderate")
    storage = data.get("storageCondition", "Ambient")
    sustainability = data.get("sustainability", "Standard")

    query_prompt = (
        f"Recommend safe packaging for: {food_name}, "
        f"Moisture: {moisture}, Fat: {fat}, Acidity: {acidity}, "
        f"Oxygen Sensitivity: {oxygen}, Light Sensitivity: {light}, "
        f"Storage: {storage}, Sustainability: {sustainability}"
    )
    reply = handle_chatbot_query(query_prompt)
    return jsonify({"recommendation": reply, "reply": reply, "status": "success"})

# -----------------------------------------------------------------------------
# Initialize DB on Startup
# -----------------------------------------------------------------------------
init_db()

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", "5000"))
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    print(f"PackSense AI Flask server starting on {host}:{port}")
    app.run(host=host, port=port, debug=False)
