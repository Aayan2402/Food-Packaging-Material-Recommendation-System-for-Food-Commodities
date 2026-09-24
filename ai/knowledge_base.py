"""
PackSense AI - Knowledge Base & Localization Module
Connects to SQLite database, initializes tables and provides translations
for English, Hindi (हिंदी), and Marathi (मराठी).
"""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "packsense.db")
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database", "schema.sql")
SEED_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database", "seed_data.sql")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(force=False):
    """Initializes or migrates the SQLite database with schema and seed data."""
    needs_full_init = not os.path.exists(DB_PATH) or force or os.path.getsize(DB_PATH) == 0
    if needs_full_init:
        conn = get_db_connection()
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        with open(SEED_PATH, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("Database initialized with schema and seed data.")
    else:
        # Run safe migrations on existing database
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cols = [row[1] for row in cur.execute("PRAGMA table_info(users)").fetchall()]
            if "role" not in cols:
                cur.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'farmer'")
                conn.commit()
            
            # Ensure demo accounts exist with active SHA-256 hashes (password: demo123)
            # sha256("demo123") = d3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791
            cur.execute("""
                INSERT OR REPLACE INTO users (name, email, password_hash, role, language, mode)
                VALUES 
                ('Ayan', 'ayanshaikhjann080808@gmail.com', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'farmer', 'en', 'farmer'),
                ('PackSense Demo User', 'demo@packsense.ai', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'farmer', 'en', 'farmer'),
                ('Demo Farmer', 'farmer@packsense.ai', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'farmer', 'en', 'farmer'),
                ('Packaging Scientist', 'lab@packsense.ai', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'industry', 'en', 'industry')
            """)
            conn.commit()
            conn.close()
            print("Database checked and user credentials verified.")
        except Exception as e:
            print(f"Database migration notice: {e}")

# ==============================================================================
# MASTER LOCALIZATION DICTIONARY (21 GLOBAL & REGIONAL LANGUAGES)
# ==============================================================================
from ai.translations import TRANSLATIONS, SUPPORTED_LANGUAGES, get_translation

def get_text(key, lang="en"):
    """Fetches localized string with fallback to English."""
    return get_translation(key, lang)
def get_food_by_name(food_name):
    """Retrieves full biochemical profile for a given food."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM foods WHERE name = ? OR name LIKE ?", (food_name, f"%{food_name}%"))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    # Fallback default commodity
    return {
        "name": food_name or "Generic Produce",
        "category": "Produce",
        "default_condition": "Fresh",
        "respiration_rate": "Medium",
        "moisture_sensitivity": "Medium",
        "fat_vulnerability": "Low",
        "ph": 5.0,
        "temp_sensitivity": "Moderate",
        "microbial_risk": "Moderate",
        "ethylene_emission": "Low",
        "standard_shelf_life_days": 5,
        "target_otr": 1800.0,
        "target_wvtr": 15.0,
        "opt_temp_c": 8.0,
        "opt_rh_pct": 85.0,
        "spoilage_mechanism": "Standard aerobic respiration and moisture transpiration."
    }

def get_all_foods():
    """Returns list of all available food commodities in the knowledge base."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM foods ORDER BY category, name")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_translation(key, lang="en"):
    """Returns localized string for a key in en, hi, or mr."""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS.get("en", {}))
    if key in lang_dict:
        return lang_dict[key]
    # Fallback to English
    return TRANSLATIONS.get("en", {}).get(key, key)

def get_all_materials():
    """Returns list of all packaging materials in the database."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM packaging_materials ORDER BY sustainability_score DESC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_climate_for_city(city_name):
    """Returns seasonal climate statistics for a given Indian city."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM climate_data WHERE city = ?", (city_name,))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    # Default inland Indian average
    return {
        "city": city_name,
        "state": "India",
        "zone": "Central Plateau",
        "summer_temp": 38.0,
        "summer_rh": 45.0,
        "monsoon_temp": 28.0,
        "monsoon_rh": 80.0,
        "winter_temp": 24.0,
        "winter_rh": 50.0,
        "humidity_stress_factor": 1.2
    }

def get_all_cities():
    """Returns list of registered cities."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT city, state, zone FROM climate_data ORDER BY city")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows
