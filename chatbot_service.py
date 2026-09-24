"""
PackSense AI – Food Safety Assistant Service
Grounded in FSSAI Packaging Regulations 2018, Maharashtra FDA Context, and BIS Standards.
"""

import os
import json
import urllib.request
import urllib.error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "packsense-chatbot", "knowledge")

# Load structured knowledge bases
def load_json(filename):
    path = os.path.join(KNOWLEDGE_DIR, filename)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    return {}

FSSAI_DATA = load_json("fssai-packaging.json")
FOOD_SAFETY_DATA = load_json("food-safety.json")
MAHA_FDA_DATA = load_json("maharashtra-fda.json")
MATERIALS_DATA = load_json("packaging-materials.json")
REFERENCES_DATA = load_json("references.json")

SYSTEM_PROMPT = """
You are PackSense AI – Food Safety Assistant, an educational AI chatbot answering questions about food safety, food packaging, FSSAI regulations, and Maharashtra FDA context.

CRITICAL BOUNDARIES & INSTRUCTIONS:
1. Role: Provide AI-assisted educational information and preliminary food-packaging recommendations. You are NOT an official FSSAI or Maharashtra FDA system, and you do not provide legal approval, certification, or formal compliance clearances.
2. Structure: Whenever appropriate (especially for packaging advice, materials, or commodities), structure your response using this exact format:
🍱 FOOD / PRODUCT: [Name of commodity or category]
📦 RECOMMENDED PACKAGING: [Specific food-grade material / laminate / container]
🛡️ REQUIRED PROTECTION: [Barrier requirements, e.g., OTR, WVTR, light block, grease barrier]
🔬 WHY: [Food chemistry decay mechanics, lipid oxidation, microbial risk, respiration]
♻️ ALTERNATIVE: [Safe food-grade alternative or sustainable option]
⚠️ FOOD-SAFETY CONSIDERATION: [Specific migration limits, contamination hazards, temperature constraints]
📚 REGULATORY REFERENCE: [FSSAI Packaging Regulations 2018, BIS Standards IS 9845, IS 10146, IS 6615, etc.]
🤖 AI NOTE: [AI-Assisted Preliminary Recommendation. Verify current standards before commercial procurement.]

3. FSSAI Regulations vs Maharashtra FDA vs Tukaram Munde:
- FSSAI: Formulates uniform national standards (Food Safety and Standards Act, 2006; Packaging Regulations 2018; Overall Migration Limit of 60 mg/kg under IS 9845; strict ban on newspaper and unapproved recycled plastics).
- Maharashtra FDA: State department enforcing FSSAI regulations, surveillance, laboratory sampling, and anti-adulteration drives across Maharashtra.
- Tukaram Munde (Senior IAS Officer): Former Commissioner of FDA Maharashtra (late 2022 to early 2023) known for aggressive enforcement raids on milk adulteration (detergents/urea), counterfeit edible oils, and festive mawa/khoya.
- MANDATORY RULE: NEVER say "Tukaram Munde created all FSSAI food packaging rules." FSSAI is a national statutory body. Always state: "These requirements arise from the applicable FSSAI/Government regulatory framework. Maharashtra FDA enforcement and public food-safety activities during the relevant period can be discussed separately."
- If you cannot verify any specific claim, date, penalty, or government resolution from official sources, you MUST explicitly state: "I could not verify this claim from an official source." Never invent dates, orders, penalties, statements, or regulations.

4. Newspaper Prohibition:
- Under Regulation 3(4) of Food Safety and Standards (Packaging) Regulations, 2018, newspaper and printed recycled paper are strictly BANNED for wrapping, serving, or absorbing oil from food.
- Reason: Printing inks contain toxic mineral oil aromatic hydrocarbons (MOAH), lead, cadmium, and naphthylamines that leach into hot or oily food in seconds. Safe alternatives: Food-grade greaseproof paper (IS 6615), butter paper, banana leaves, SS304.

Keep your answers clear, professional, concise, and easy to understand for food businesses, students, and citizens.
"""

def call_gemini_api(user_message, history=None):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"
    
    # Build contents with history if available
    contents = []
    if history:
        for msg in history[-4:]:
            role = "user" if msg.get("role") == "user" else "model"
            contents.append({"role": role, "parts": [{"text": msg.get("content", "")}]})
    
    contents.append({"role": "user", "parts": [{"text": user_message}]})

    payload = {
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": contents,
        "generationConfig": {
            "temperature": 0.25,
            "maxOutputTokens": 950
        }
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts:
                    return parts[0].get("text", "")
    except Exception as e:
        print(f"Gemini API request failed: {e}")
        return None

def fallback_knowledge_query(query):
    """Accurate offline knowledge-base query parser matching exact user inquiries."""
    q = query.lower()

    # 1. Newspaper Question
    if any(k in q for k in ["newspaper", "news paper", "printed paper", "wrapping in newspaper"]):
        return (
            "🍱 FOOD / PRODUCT: Cooked street foods, fried snacks (samosas, vada pav), bakery items, fresh produce\n"
            "📦 RECOMMENDED PACKAGING: Certified Food-Grade Greaseproof Paper (IS 6615), Butter Paper, or clean plant leaf wraps\n"
            "🛡️ REQUIRED PROTECTION: Grease barrier (Kit 7-12) and zero toxic chemical migration\n"
            "🔬 WHY: Newspaper printing inks contain carcinogenic mineral oil aromatic hydrocarbons (MOAH), lead, cadmium, and naphthylamines. Hot and oily food leaches these solvents within seconds, posing severe cancer and toxicity risks.\n"
            "♻️ ALTERNATIVE: Food-grade stainless steel plates (SS304), certified parchment paper, or fresh banana leaves\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: Regulation 3(4) of Food Safety and Standards (Packaging) Regulations, 2018 strictly bans using newspaper for wrapping, storing, or absorbing oil from food across India.\n"
            "📚 REGULATORY REFERENCE: FSSAI Packaging Regulations 2018 (Section 3(4)); BIS IS 6615; Maharashtra FDA public advisory notifications.\n"
            "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Newspaper must NEVER be used for food contact under any circumstance."
        )

    # 2. Food-Grade Packaging Definition
    if any(k in q for k in ["what is food-grade", "what is food grade", "food-grade packaging", "food grade packaging"]):
        return (
            "🍱 FOOD / PRODUCT: Universal Food Contact Materials & Articles\n"
            "📦 RECOMMENDED PACKAGING: Materials certified under prescribed Indian Standards (e.g., IS 10146 for PE, IS 10910 for PP, IS 1382 for Glass, IS 1997 for Tinplate)\n"
            "🛡️ REQUIRED PROTECTION: Chemical inertness, zero organoleptic degradation, and compliance with Overall Migration Limit (< 60 mg/kg under IS 9845)\n"
            "🔬 WHY: Food-grade indicates that the polymer, paper, metal, or glass has been formulated, tested, and certified safe for direct contact with food without leaching harmful monomers, plasticizers, or toxic heavy metals.\n"
            "♻️ ALTERNATIVE: Type III Neutral Soda-Lime Glass or Food-Grade Stainless Steel (SS304/SS316)\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: Recycled untreated plastics are strictly prohibited in primary food packaging under Regulation 3(2) of FSSAI Packaging Regulations 2018 unless specifically certified under FSSAI rPET guidelines.\n"
            "📚 REGULATORY REFERENCE: Food Safety and Standards (Packaging) Regulations, 2018; BIS IS 9845:2020 migration testing.\n"
            "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Suitability always depends on specific food chemistry (acidic, oily, aqueous) and operating temperature."
        )

    # 3. Oily / Fatty Foods
    if any(k in q for k in ["oily food", "fatty food", "fried food", "namkeen", "chips", "oil"]):
        return (
            "🍱 FOOD / PRODUCT: Oily Foods, Fried Namkeen, Potato Chips, Roasted Nuts\n"
            "📦 RECOMMENDED PACKAGING: Multi-layer laminate: Biaxially Oriented Polypropylene (BOPP) / Metallized BOPP / Polyethylene with Nitrogen (N₂) gas flushing\n"
            "🛡️ REQUIRED PROTECTION: Ultra-high oxygen barrier (OTR < 15 cc/m²/day), zero light transmission, and grease resistance\n"
            "🔬 WHY: Unsaturated lipids undergo rapid free radical oxidation when exposed to oxygen and light, producing rancid off-flavors (hexanals). Metallized film completely blocks UV light and oxygen.\n"
            "♻️ ALTERNATIVE: Food-grade Greaseproof Paper (IS 6615) with bio-wax coating for short-duration shelf life (< 48 hrs)\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: Never pack hot fried snacks directly into low-grade polyethylene bags; high oil temperatures accelerate plasticizer and phthalate migration.\n"
            "📚 REGULATORY REFERENCE: FSSAI Packaging Regulations, 2018 (Schedule I: IS 10910, IS 1060).\n"
            "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Nitrogen flush with < 2% residual O₂ extends shelf life by 400%."
        )

    # 4. Milk & Dairy
    if any(k in q for k in ["milk", "dairy", "paneer", "curd"]):
        return (
            "🍱 FOOD / PRODUCT: Fresh Pasteurized Milk or Ambient Long-Life (UHT) Milk\n"
            "📦 RECOMMENDED PACKAGING: 3/5-layer co-extruded LDPE/LLDPE pouch with carbon-black light barrier layer (pasteurized) or 6-layer Aseptic Brick Carton (UHT)\n"
            "🛡️ REQUIRED PROTECTION: Complete light barrier (blocks riboflavin photolysis), hermetic microbial seal, and pinhole resistance\n"
            "🔬 WHY: Milk contains Vitamin B2 (riboflavin), which is a photosensitizer. Exposure to daylight triggers riboflavin photolysis within 2 hours, resulting in oxidized cardboard off-flavor and nutrient loss.\n"
            "♻️ ALTERNATIVE: Type III Amber Glass bottles or HDPE bottles with UV absorbers\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: Cold-chain maintenance (<= 4°C) is mandatory for pasteurized pouches to prevent rapid bacterial spoilage (Listeria, Salmonella).\n"
            "📚 REGULATORY REFERENCE: FSSAI Packaging Regulations, 2018; BIS IS 10146 (Polyethylene for food contact).\n"
            "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Maintain tamper-evident closures on all consumer units."
        )

    # 5. Tukaram Munde & Maharashtra FDA Context
    if any(k in q for k in ["tukaram", "munde", "maharashtra fda", "fda maharashtra"]):
        return (
            "🍱 FOOD / PRODUCT: Regulatory Administration & State Food Safety Enforcement\n"
            "📦 RECOMMENDED PACKAGING: FSSAI-compliant certified packaging and tamper-evident sealing\n"
            "🛡️ REQUIRED PROTECTION: Strict institutional distinction between Union statutory regulation and State administrative enforcement\n"
            "🔬 WHY: These requirements arise from the applicable FSSAI/Government regulatory framework. Maharashtra FDA enforcement and public food-safety activities during the relevant period can be discussed separately.\n"
            "♻️ ALTERNATIVE: N/A (Statutory framework)\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: During his tenure as Commissioner of FDA Maharashtra (late 2022 to early 2023), Tukaram Munde led intensive statewide crackdowns on adulterated milk (synthetic milk, urea, detergents), spurious festive mawa/khoya, loose unbranded edible oils, and non-compliant street food packaging. Note: FSSAI formulates the national packaging regulations, while Maharashtra FDA enforces them at state level.\n"
            "📚 REGULATORY REFERENCE: Food Safety and Standards Act, 2006; Maharashtra FDA Department Orders.\n"
            "🤖 AI NOTE: AI-Assisted Educational Context. If a specific enforcement claim cannot be verified from an official government gazette, the assistant notes: 'I could not verify this claim from an official source.'"
        )

    # 6. Spices
    if any(k in q for k in ["spice", "spices", "masala", "chilli powder", "turmeric"]):
        return (
            "🍱 FOOD / PRODUCT: Ground Spices, Curry Powders, Whole Spices\n"
            "📦 RECOMMENDED PACKAGING: PET / Metallized PET / Polyethylene laminated pouches\n"
            "🛡️ REQUIRED PROTECTION: High moisture barrier (WVTR < 0.5 g/m²/day), aroma retention, and light barrier\n"
            "🔬 WHY: Spices lose volatile essential oils (curcumin, capsaicin, piperine) and aroma when exposed to air. Moisture absorption causes caking and fungal aflatoxin risk.\n"
            "♻️ ALTERNATIVE: Hermetically sealed glass jars or lacquered tinplate canisters\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: Do not use unlined paper or porous plastic bags; aroma scalping and oil bleeding can degrade seal strength.\n"
            "📚 REGULATORY REFERENCE: FSSAI Packaging Regulations, 2018 (Schedule I: IS 12252, IS 1060).\n"
            "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Ensure tamper-evident induction heat seal."
        )

    # 7. Dry Food & Pulses
    if any(k in q for k in ["dry food", "pulse", "grains", "cereal", "flour"]):
        return (
            "🍱 FOOD / PRODUCT: Dry Food, Cereals, Pulses, Wheat Flour (Atta)\n"
            "📦 RECOMMENDED PACKAGING: Multi-wall Kraft paper sacks with woven PP liner or Biaxially Oriented Polypropylene (BOPP) laminated bags\n"
            "🛡️ REQUIRED PROTECTION: Moisture barrier (prevents fungal mold) and puncture resistance\n"
            "🔬 WHY: Dry foods with moisture < 12% are vulnerable to ambient relative humidity; moisture ingress increases water activity (aw > 0.65), triggering Aspergillus mold and insect infestation.\n"
            "♻️ ALTERNATIVE: Recyclable mono-material HDPE woven sacks conforming to IS 14887\n"
            "⚠️ FOOD-SAFETY CONSIDERATION: Avoid untreated second-hand jute bags previously used for fertilizers or non-food chemicals.\n"
            "📚 REGULATORY REFERENCE: FSSAI Packaging Regulations, 2018; BIS IS 6615, IS 10146.\n"
            "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Store in dry, well-ventilated conditions."
        )

    # Default Structured Guidance
    return (
        f"🍱 FOOD / PRODUCT: Food Commodity Inquired ({query[:50]})\n"
        "📦 RECOMMENDED PACKAGING: Food-Grade Multi-layer Barrier Laminate or Certified Paperboard\n"
        "🛡️ REQUIRED PROTECTION: Barrier tailored to moisture (WVTR), oxygen (OTR), light, and microbial conditions\n"
        "🔬 WHY: Safe packaging must preserve freshness, block environmental contaminants, and comply with inertness requirements.\n"
        "♻️ ALTERNATIVE: Type III Neutral Soda-Lime Glass or Biodegradable Paperboard with Bio-Wax Coating\n"
        "⚠️ FOOD-SAFETY CONSIDERATION: Packaging must strictly satisfy Overall Migration Limits (< 60 mg/kg under IS 9845) and zero chemical leaching into food.\n"
        "📚 REGULATORY REFERENCE: Food Safety and Standards (Packaging) Regulations, 2018; BIS Standards.\n"
        "🤖 AI NOTE: AI-Assisted Preliminary Recommendation. Launch the 12-factor wizard for a granular chemical analysis."
    )

def handle_chatbot_query(message, history=None):
    """Processes user query using Gemini API with automatic fallback to verified local knowledge base."""
    # Try Gemini 3.6 Flash first if configured
    gemini_reply = call_gemini_api(message, history)
    if gemini_reply and len(gemini_reply.strip()) > 30:
        return gemini_reply

    # Otherwise return verified local rule-based knowledge
    return fallback_knowledge_query(message)
