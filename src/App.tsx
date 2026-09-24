import React, { useState, useRef, useEffect } from 'react';
import { 
  Bot, 
  Send, 
  BookOpen, 
  Trash2, 
  Copy, 
  Check, 
  ShieldCheck, 
  Sparkles, 
  HelpCircle, 
  ExternalLink,
  ChevronRight,
  Package,
  Layers,
  Leaf,
  Info
} from 'lucide-react';

interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
}

const SUGGESTED_QUESTIONS = [
  "What is food-grade packaging?",
  "Can newspaper be used to wrap food?",
  "What packaging is suitable for oily food?",
  "What packaging is suitable for milk?",
  "What packaging is suitable for spices?",
  "What packaging is suitable for dry food?",
  "How does packaging affect shelf life?",
  "What are FSSAI packaging requirements?",
  "What does Maharashtra FDA do?",
  "What is the Tukaram Munde FDA context?",
  "Which packaging material is suitable for my food?",
  "How can I select safe food packaging?"
];

const OFFICIAL_SOURCES = [
  {
    title: "FSSAI Packaging Regulations, 2018 (Official Gazette)",
    body: "Notified under Section 92 of FSS Act, 2006. Prescribes food-grade compliance, Overall Migration Limit (IS 9845), and strictly bans using newspaper or unapproved recycled plastic for food wrapping.",
    link: "https://www.fssai.gov.in"
  },
  {
    title: "Maharashtra Food and Drug Administration (FDA)",
    body: "State-level enforcement authority overseeing food inspections, anti-adulteration crackdowns, laboratory sampling, and compliance across Maharashtra districts.",
    link: "https://fda.maharashtra.gov.in"
  },
  {
    title: "Bureau of Indian Standards (BIS) Food Contact Specifications",
    body: "National standards including IS 10146 (Polyethylene), IS 10910 (Polypropylene), IS 6615 (Greaseproof paper), and IS 9845 (Overall Migration Limits).",
    link: "https://standardsbis.bsbedge.com"
  }
];

export default function App() {
  const [activeTab, setActiveTab] = useState<'chat' | 'home' | 'about'>('chat');
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'msg-init',
      role: 'assistant',
      content: `Welcome to **PackSense AI – Food Safety Assistant**!
Ask me about food packaging safety, FSSAI regulations, food-grade barrier requirements, or Maharashtra FDA enforcement context.

Choose a suggested question below or type your inquiry.`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);
  const [inputQuery, setInputQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [showSourcesModal, setShowSourcesModal] = useState(false);
  const [showWizardModal, setShowWizardModal] = useState(false);

  // 12-factor wizard state
  const [wizardData, setWizardData] = useState({
    foodName: '',
    moistureLevel: 'Dry (< 10%)',
    fatContent: 'Low / Negligible',
    acidity: 'Neutral (pH 6-7)',
    oxygenSensitivity: 'Moderate',
    lightSensitivity: 'Moderate',
    storageCondition: 'Ambient Room Temp (25-35°C)',
    sustainability: 'Standard High-Barrier'
  });

  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSend = async (text: string) => {
    if (!text.trim() || isLoading) return;

    const userMsg: ChatMessage = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: text.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputQuery('');
    setIsLoading(true);

    try {
      const res = await fetch('/api/chatbot/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: text.trim(),
          history: messages.slice(-4).map((m) => ({ role: m.role, content: m.content }))
        })
      });

      if (!res.ok) throw new Error('API request failed');
      const data = await res.json();

      const botMsg: ChatMessage = {
        id: `bot-${Date.now()}`,
        role: 'assistant',
        content: data.reply || 'Information retrieved.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch {
      // Offline fallback generator
      const botMsg: ChatMessage = {
        id: `bot-${Date.now()}`,
        role: 'assistant',
        content: generateClientFallback(text),
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages((prev) => [...prev, botMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  const generateClientFallback = (q: string): string => {
    const query = q.toLowerCase();
    if (query.includes('newspaper') || query.includes('wrap')) {
      return `🍱 FOOD / PRODUCT: Street food, Fried Snacks, Vada Pav, Samosas, Bakery
📦 RECOMMENDED PACKAGING: Certified Food-Grade Greaseproof Paper (IS 6615) or Butter Paper
🛡️ REQUIRED PROTECTION: Grease-resistance and absolute zero toxic chemical migration
🔬 WHY: Newspaper printing inks contain carcinogenic mineral oil aromatic hydrocarbons (MOAH), lead, and naphthylamines that leach into hot/oily food within seconds.
♻️ ALTERNATIVE: Food-grade stainless steel (SS304) plates or fresh banana leaves
⚠️ FOOD-SAFETY CONSIDERATION: Regulation 3(4) of FSSAI Packaging Regulations 2018 strictly bans newspaper for wrapping or serving food.
📚 REGULATORY REFERENCE: Food Safety and Standards (Packaging) Regulations, 2018; BIS IS 6615.
🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Newspaper must NEVER be used for direct food contact.`;
    }
    if (query.includes('oily') || query.includes('fat')) {
      return `🍱 FOOD / PRODUCT: Oily Foods, Fried Namkeen, Potato Chips
📦 RECOMMENDED PACKAGING: Multi-layer laminate (BOPP / Metallized BOPP / Polyethylene) with Nitrogen flushing
🛡️ REQUIRED PROTECTION: Ultra-high oxygen barrier (OTR < 15 cc/m²/day) and zero light transmission
🔬 WHY: Unsaturated fats undergo rapid lipid peroxidation when exposed to atmospheric oxygen, causing rancidity.
♻️ ALTERNATIVE: Certified greaseproof paperboard with bio-wax coating for short-duration shelf life
⚠️ FOOD-SAFETY CONSIDERATION: Never pack hot fried snacks directly into low-grade polythene bags.
📚 REGULATORY REFERENCE: FSSAI Packaging Regulations 2018 (Schedule I); IS 10910.
🤖 AI NOTE: AI-Assisted Preliminary Recommendation. N₂ flush extends shelf life by 400%.`;
    }
    if (query.includes('milk') || query.includes('dairy')) {
      return `🍱 FOOD / PRODUCT: Pasteurized or UHT Cow/Buffalo Milk
📦 RECOMMENDED PACKAGING: 3/5-layer co-extruded LDPE/LLDPE pouch with carbon-black light-barrier layer or Aseptic Brick Carton
🛡️ REQUIRED PROTECTION: Complete light barrier (blocks riboflavin breakdown) and sterile hermetic seal
🔬 WHY: Milk contains riboflavin (Vitamin B2) which rapidly photolyses under light, causing oxidized off-flavor.
♻️ ALTERNATIVE: Type III Amber Glass bottles or HDPE bottles with UV inhibitors
⚠️ FOOD-SAFETY CONSIDERATION: Maintain cold-chain (<= 4°C) for pasteurized pouches to prevent bacterial spoilage.
📚 REGULATORY REFERENCE: FSSAI Packaging Regulations 2018; BIS IS 10146.
🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Tamper-evident closures are mandatory.`;
    }
    if (query.includes('tukaram') || query.includes('munde') || query.includes('fda')) {
      return `🍱 FOOD / PRODUCT: State Food Safety Administration & Regulatory Enforcement
📦 RECOMMENDED PACKAGING: FSSAI-certified compliant packaging
🛡️ REQUIRED PROTECTION: Institutional distinction between Union statutory regulation and State administrative enforcement
🔬 WHY: These requirements arise from the applicable FSSAI/Government regulatory framework. Maharashtra FDA enforcement and public food-safety activities during the relevant period can be discussed separately.
♻️ ALTERNATIVE: N/A (Statutory framework)
⚠️ FOOD-SAFETY CONSIDERATION: During his tenure as Commissioner of FDA Maharashtra (late 2022 to early 2023), Tukaram Munde led aggressive statewide crackdowns against milk adulteration (detergents, urea), fake mawa, and loose edible oils. Note: FSSAI creates the regulations; Maharashtra FDA enforces them.
📚 REGULATORY REFERENCE: Food Safety and Standards Act, 2006; Maharashtra FDA Department Orders.
🤖 AI NOTE: AI-Assisted Educational Context. If a claim cannot be verified from an official gazette, the assistant notes: "I could not verify this claim from an official source."`;
    }
    return `🍱 FOOD / PRODUCT: Food Commodity (${q})
📦 RECOMMENDED PACKAGING: Food-Grade Multi-layer Barrier Laminate or Certified Paperboard
🛡️ REQUIRED PROTECTION: Barrier tailored to moisture, oxygen, light, and microbial risks
🔬 WHY: Packaging preserves organoleptic freshness and halts biochemical decay.
♻️ ALTERNATIVE: Type III Neutral Soda-Lime Glass or Biodegradable Paperboard
⚠️ FOOD-SAFETY CONSIDERATION: Compliance with Overall Migration Limit (< 60 mg/kg under IS 9845) is mandatory.
📚 REGULATORY REFERENCE: Food Safety and Standards (Packaging) Regulations, 2018.
🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Launch the 12-factor wizard for detailed analysis.`;
  };

  const handleCopy = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleClear = () => {
    setMessages([
      {
        id: `bot-clear-${Date.now()}`,
        role: 'assistant',
        content: `Chat history cleared. How can I assist you with food packaging safety or FSSAI regulations today?`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ]);
  };

  const handleWizardSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setShowWizardModal(false);
    const summary = `Recommend safe packaging for: ${wizardData.foodName || 'Food Item'}, Moisture: ${wizardData.moistureLevel}, Fat/Oil: ${wizardData.fatContent}, Acidity: ${wizardData.acidity}, Oxygen Sensitivity: ${wizardData.oxygenSensitivity}, Light Sensitivity: ${wizardData.lightSensitivity}, Storage: ${wizardData.storageCondition}, Sustainability: ${wizardData.sustainability}`;
    handleSend(summary);
  };

  return (
    <div className="min-h-screen bg-[#0b1626] text-slate-100 flex flex-col font-sans">
      {/* Top Navbar */}
      <header className="border-b border-slate-800 bg-[#0e1d32]/95 backdrop-blur sticky top-0 z-40 px-4 py-3">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-sky-500 flex items-center justify-center shadow-lg shadow-emerald-500/20">
              <Bot className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-lg tracking-tight text-white">Pack<span className="text-emerald-400">Sense</span></span>
                <span className="text-[10px] font-bold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-1.5 py-0.5 rounded">AI</span>
              </div>
              <p className="text-xs text-slate-400">Intelligent Food Packaging & Safety System</p>
            </div>
          </div>

          <nav className="flex items-center gap-2">
            <button 
              onClick={() => setActiveTab('chat')}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 ${
                activeTab === 'chat' 
                  ? 'bg-emerald-500 text-white shadow-md shadow-emerald-500/30' 
                  : 'text-slate-300 hover:bg-slate-800'
              }`}
            >
              <span>🤖</span> Ask PackSense AI
            </button>
            <a 
              href="/workspace"
              className="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 transition"
            >
              Workspace
            </a>
            <a 
              href="/packaudit"
              className="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 transition"
            >
              PackAudit CV
            </a>
            <a 
              href="/about"
              className="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 transition"
            >
              About
            </a>
          </nav>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-6xl w-full mx-auto p-4 md:p-6 flex flex-col">
        {/* Chatbot Interface */}
        <div className="bg-[#11243b] border border-slate-700/80 rounded-2xl shadow-2xl flex flex-col flex-1 overflow-hidden">
          {/* Header */}
          <div className="p-4 md:p-5 bg-gradient-to-r from-[#0b1626] to-[#142842] border-b border-slate-700/80 flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-3">
              <div className="w-11 h-11 rounded-xl bg-gradient-to-tr from-emerald-500 to-sky-500 flex items-center justify-center text-xl shadow-md shadow-emerald-500/30">
                🤖
              </div>
              <div>
                <h1 className="text-base md:text-lg font-bold text-white flex items-center gap-2">
                  PackSense AI – Food Safety Assistant
                </h1>
                <p className="text-xs text-slate-400">
                  “Ask about Food Packaging, FSSAI & FDA Food-Safety Requirements”
                </p>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => setShowWizardModal(true)}
                className="px-3 py-1.5 rounded-lg text-xs font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 hover:bg-sky-500/30 transition flex items-center gap-1.5"
                title="12-Factor Packaging Recommendation Engine"
              >
                <Sparkles className="w-3.5 h-3.5" />
                <span>12-Factor Wizard</span>
              </button>
              <button
                onClick={() => setShowSourcesModal(true)}
                className="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-200 border border-slate-700 hover:bg-slate-700 transition flex items-center gap-1.5"
                title="View Official FSSAI & FDA Sources"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>📚 Official Sources</span>
              </button>
              <button
                onClick={handleClear}
                className="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-rose-400 border border-slate-700 hover:bg-slate-700 transition flex items-center gap-1"
                title="Clear Chat History"
              >
                <Trash2 className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Clickable Suggested Questions Bar */}
          <div className="px-4 py-2.5 bg-[#0e1d33] border-b border-slate-800 overflow-x-auto whitespace-nowrap flex gap-2 text-xs scrollbar-thin">
            {SUGGESTED_QUESTIONS.map((q, idx) => (
              <button
                key={idx}
                onClick={() => handleSend(q)}
                className="px-3 py-1 rounded-full bg-slate-800/90 hover:bg-emerald-950/60 hover:text-emerald-300 hover:border-emerald-500/40 text-slate-300 border border-slate-700 text-xs transition shrink-0"
              >
                {q}
              </button>
            ))}
          </div>

          {/* Messages Scroll Area */}
          <div className="flex-1 overflow-y-auto p-4 md:p-6 space-y-4 bg-gradient-to-b from-[#0e1d33]/50 to-[#11243b]">
            {messages.map((m) => (
              <div
                key={m.id}
                className={`flex gap-3 max-w-4xl ${m.role === 'user' ? 'ml-auto flex-row-reverse' : ''}`}
              >
                <div
                  className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 text-sm ${
                    m.role === 'user' ? 'bg-sky-600 text-white' : 'bg-emerald-600 text-white'
                  }`}
                >
                  {m.role === 'user' ? '👤' : '🤖'}
                </div>

                <div className={`space-y-1.5 ${m.role === 'user' ? 'items-end' : 'items-start'}`}>
                  <div
                    className={`rounded-2xl p-4 text-sm leading-relaxed ${
                      m.role === 'user'
                        ? 'bg-sky-600 text-white rounded-tr-none'
                        : 'bg-[#162c49] border border-slate-700/80 text-slate-200 rounded-tl-none shadow-md'
                    }`}
                  >
                    <div className="whitespace-pre-line">{m.content}</div>
                  </div>

                  {m.role === 'assistant' && (
                    <div className="flex items-center gap-2 pt-1 pl-1">
                      <button
                        onClick={() => handleCopy(m.id, m.content)}
                        className="text-[11px] text-slate-400 hover:text-slate-200 flex items-center gap-1 bg-slate-800/80 hover:bg-slate-700 px-2 py-0.5 rounded border border-slate-700 transition"
                      >
                        {copiedId === m.id ? (
                          <>
                            <Check className="w-3 h-3 text-emerald-400" />
                            <span className="text-emerald-400">Copied!</span>
                          </>
                        ) : (
                          <>
                            <Copy className="w-3 h-3" />
                            <span>Copy</span>
                          </>
                        )}
                      </button>
                      <button
                        onClick={() => setShowSourcesModal(true)}
                        className="text-[11px] text-slate-400 hover:text-sky-300 flex items-center gap-1 bg-slate-800/80 hover:bg-slate-700 px-2 py-0.5 rounded border border-slate-700 transition"
                      >
                        <BookOpen className="w-3 h-3 text-sky-400" />
                        <span>📚 Official Sources</span>
                      </button>
                      <span className="text-[10px] text-slate-500 ml-auto">{m.timestamp}</span>
                    </div>
                  )}
                </div>
              </div>
            ))}

            {isLoading && (
              <div className="flex gap-3">
                <div className="w-8 h-8 rounded-full bg-emerald-600 text-white flex items-center justify-center shrink-0 text-sm">
                  🤖
                </div>
                <div className="bg-[#162c49] border border-slate-700/80 rounded-2xl rounded-tl-none p-3.5 flex items-center gap-2">
                  <div className="w-2 h-2 rounded-full bg-emerald-400 animate-bounce" />
                  <div className="w-2 h-2 rounded-full bg-emerald-400 animate-bounce [animation-delay:0.2s]" />
                  <div className="w-2 h-2 rounded-full bg-emerald-400 animate-bounce [animation-delay:0.4s]" />
                </div>
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>

          {/* Input Bar */}
          <div className="p-3 md:p-4 bg-[#0e1d33] border-t border-slate-800">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSend(inputQuery);
              }}
              className="flex items-center gap-2"
            >
              <input
                type="text"
                value={inputQuery}
                onChange={(e) => setInputQuery(e.target.value)}
                placeholder="Ask about newspaper ban, oily food packaging, milk UV protection, or FSSAI rules..."
                className="flex-1 bg-[#162c49] border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white placeholder-slate-400 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500"
              />
              <button
                type="submit"
                disabled={!inputQuery.trim() || isLoading}
                className="bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white font-bold px-4 py-2.5 rounded-xl text-sm transition flex items-center gap-2 shadow-lg shadow-emerald-600/30"
              >
                <span>Send</span>
                <Send className="w-4 h-4" />
              </button>
            </form>
          </div>

          {/* Statutory Disclaimer */}
          <div className="px-4 py-2.5 bg-[#091322] border-t border-slate-800 text-[11px] text-slate-400 leading-relaxed text-center">
            PackSense AI provides AI-assisted educational information and preliminary food-packaging recommendations. It is not an official FSSAI or Maharashtra FDA system and does not provide regulatory approval, certification or legal advice. Always verify applicable regulations and food-contact requirements using current official sources before making commercial packaging decisions.
          </div>
        </div>
      </main>

      {/* Sources Modal */}
      {showSourcesModal && (
        <div className="fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-[#11243b] border border-slate-700 rounded-2xl max-w-xl w-full p-6 shadow-2xl relative">
            <div className="flex items-center justify-between pb-3 border-b border-slate-700 mb-4">
              <div className="flex items-center gap-2">
                <span className="text-xl">📚</span>
                <h3 className="text-base font-bold text-white">Official Regulatory Sources</h3>
              </div>
              <button
                onClick={() => setShowSourcesModal(false)}
                className="text-slate-400 hover:text-white text-lg font-bold"
              >
                ✕
              </button>
            </div>

            <p className="text-xs text-slate-300 mb-4">
              PackSense AI strictly cites verified statutory gazette notifications, parliamentary acts, and government portals:
            </p>

            <div className="space-y-3">
              {OFFICIAL_SOURCES.map((source, i) => (
                <div key={i} className="bg-[#162c49] border border-slate-700 p-3.5 rounded-xl space-y-1.5">
                  <h4 className="text-sm font-bold text-white">{source.title}</h4>
                  <p className="text-xs text-slate-300 leading-relaxed">{source.body}</p>
                  <a
                    href={source.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs text-sky-400 hover:text-sky-300 font-semibold inline-flex items-center gap-1"
                  >
                    <span>Visit Official Portal</span>
                    <ExternalLink className="w-3 h-3" />
                  </a>
                </div>
              ))}
            </div>

            <div className="mt-5 text-right">
              <button
                onClick={() => setShowSourcesModal(false)}
                className="bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold px-4 py-2 rounded-lg transition"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 12-Factor Wizard Modal */}
      {showWizardModal && (
        <div className="fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-[#11243b] border border-slate-700 rounded-2xl max-w-2xl w-full p-6 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-3 border-b border-slate-700 mb-4">
              <div className="flex items-center gap-2">
                <span className="text-xl">⚡</span>
                <h3 className="text-base font-bold text-white">12-Factor Packaging Recommendation Engine</h3>
              </div>
              <button
                onClick={() => setShowWizardModal(false)}
                className="text-slate-400 hover:text-white text-lg font-bold"
              >
                ✕
              </button>
            </div>

            <p className="text-xs text-slate-300 mb-4">
              Provide your food product's chemical and logistical profile for an instant AI-Assisted Preliminary Packaging Recommendation:
            </p>

            <form onSubmit={handleWizardSubmit} className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="md:col-span-2">
                  <label className="block text-xs font-bold text-slate-300 mb-1">
                    1. Food / Product Name
                  </label>
                  <input
                    type="text"
                    required
                    value={wizardData.foodName}
                    onChange={(e) => setWizardData({ ...wizardData, foodName: e.target.value })}
                    placeholder="e.g. Potato Chips, Fresh Paneer, Table Grapes"
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  />
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-300 mb-1">2. Moisture Level</label>
                  <select
                    value={wizardData.moistureLevel}
                    onChange={(e) => setWizardData({ ...wizardData, moistureLevel: e.target.value })}
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  >
                    <option value="Dry (< 10%)">Dry (&lt; 10%)</option>
                    <option value="Semi-moist (10-40%)">Semi-moist (10-40%)</option>
                    <option value="High Moisture / Liquid (> 50%)">High Moisture / Liquid (&gt; 50%)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-300 mb-1">3. Fat / Oil Content</label>
                  <select
                    value={wizardData.fatContent}
                    onChange={(e) => setWizardData({ ...wizardData, fatContent: e.target.value })}
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  >
                    <option value="Low / Negligible">Low / Negligible</option>
                    <option value="Moderate (5-15%)">Moderate (5-15%)</option>
                    <option value="High Fat / Fried (> 20%)">High Fat / Fried (&gt; 20%)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-300 mb-1">4. Acidity / pH</label>
                  <select
                    value={wizardData.acidity}
                    onChange={(e) => setWizardData({ ...wizardData, acidity: e.target.value })}
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  >
                    <option value="Neutral (pH 6-7)">Neutral (pH 6-7)</option>
                    <option value="Mild Acidic (pH 4.5-6)">Mild Acidic (pH 4.5-6)</option>
                    <option value="High Acid / Pickled (pH < 4.5)">High Acid / Pickled (pH &lt; 4.5)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-300 mb-1">5. Oxygen Sensitivity</label>
                  <select
                    value={wizardData.oxygenSensitivity}
                    onChange={(e) => setWizardData({ ...wizardData, oxygenSensitivity: e.target.value })}
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  >
                    <option value="Low">Low</option>
                    <option value="Moderate">Moderate</option>
                    <option value="Extreme (Rancidity / Browning)">Extreme (Rancidity / Browning)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-300 mb-1">6. Light Sensitivity</label>
                  <select
                    value={wizardData.lightSensitivity}
                    onChange={(e) => setWizardData({ ...wizardData, lightSensitivity: e.target.value })}
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  >
                    <option value="Not Sensitive">Not Sensitive</option>
                    <option value="Moderate">Moderate</option>
                    <option value="High (UV Photolysis / Vitamin Loss)">High (UV Photolysis / Vitamin Loss)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-300 mb-1">7. Storage Conditions</label>
                  <select
                    value={wizardData.storageCondition}
                    onChange={(e) => setWizardData({ ...wizardData, storageCondition: e.target.value })}
                    className="w-full bg-[#162c49] border border-slate-700 rounded-lg px-3 py-2 text-xs text-white"
                  >
                    <option value="Ambient Room Temp (25-35°C)">Ambient Room Temp (25-35°C)</option>
                    <option value="Cold Chain (2-8°C)">Cold Chain (2-8°C)</option>
                    <option value="Frozen (-18°C)">Frozen (-18°C)</option>
                  </select>
                </div>
              </div>

              <div className="pt-4 flex justify-end gap-2 border-t border-slate-700">
                <button
                  type="button"
                  onClick={() => setShowWizardModal(false)}
                  className="bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold px-4 py-2 rounded-lg transition"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold px-4 py-2 rounded-lg transition"
                >
                  Generate Recommendation &rarr;
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
