-- PackSense AI - Database Schema
-- SIH Problem Statement 236: AI-Based Intelligent Food Packaging Material Recommendation System

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS foods;
DROP TABLE IF EXISTS packaging_materials;
DROP TABLE IF EXISTS climate_data;
DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS analyses;
DROP TABLE IF EXISTS packaudit_results;
DROP TABLE IF EXISTS recommendations;
DROP TABLE IF EXISTS translations;

-- 1. Users Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'farmer',
    language TEXT DEFAULT 'en',
    mode TEXT DEFAULT 'farmer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Foods Table (Biochemical Knowledge Base)
CREATE TABLE foods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL, -- Fruit, Vegetable, Snack, Dairy, Meat, Bakery
    default_condition TEXT DEFAULT 'Fresh',
    respiration_rate TEXT NOT NULL, -- Low, Medium, High, Extreme
    moisture_sensitivity TEXT NOT NULL, -- Low, Medium, High, Extreme
    fat_vulnerability TEXT NOT NULL, -- Low, Medium, High, Extreme (Lipid oxidation risk)
    ph REAL NOT NULL,
    temp_sensitivity TEXT NOT NULL, -- Low, Moderate, High, Severe
    microbial_risk TEXT NOT NULL, -- Low, Moderate, High, Critical
    ethylene_emission TEXT NOT NULL, -- None, Low, Medium, High
    standard_shelf_life_days INTEGER NOT NULL,
    target_otr REAL NOT NULL, -- cc/m2/day
    target_wvtr REAL NOT NULL, -- g/m2/day
    opt_temp_c REAL NOT NULL,
    opt_rh_pct REAL NOT NULL,
    spoilage_mechanism TEXT NOT NULL,
    notes TEXT
);

-- 3. Packaging Materials Table
CREATE TABLE packaging_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_name TEXT NOT NULL UNIQUE,
    material_type TEXT NOT NULL, -- Conventional Plastic, Multi-layer Foil, Biopolymer
    ot_r REAL NOT NULL, -- cc/m2/day
    wvtr REAL NOT NULL, -- g/m2/day
    thickness_micron INTEGER NOT NULL,
    gauge INTEGER NOT NULL, -- Indian industry standard (gauge = micron * 4)
    flexibility TEXT NOT NULL, -- Rigid, Semi-Rigid, Highly Flexible
    transparency TEXT NOT NULL, -- Crystal Clear, Semi-Transparent, Opaque
    moisture_barrier TEXT NOT NULL, -- Low, Medium, High, Exceptional
    oxygen_barrier TEXT NOT NULL, -- Low, Medium, High, Exceptional
    light_barrier TEXT NOT NULL, -- None, Moderate, Complete
    biodegradable INTEGER NOT NULL DEFAULT 0, -- 0 = No, 1 = Yes
    industrial_compost_only INTEGER NOT NULL DEFAULT 0, -- Nuance for PLA
    estimated_cost_inr REAL NOT NULL, -- Cost per standard pouch/tray (INR)
    sustainability_score REAL NOT NULL, -- Scale 1.0 to 10.0
    recommended_food TEXT,
    environmental_nuance TEXT,
    notes TEXT
);

-- 4. Climate Data Table (Indian Regional Climatology)
CREATE TABLE climate_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL UNIQUE,
    state TEXT NOT NULL,
    zone TEXT NOT NULL, -- Western Plateau, Coromandel Coast, Northern Plains, etc.
    summer_temp REAL NOT NULL,
    summer_rh REAL NOT NULL,
    monsoon_temp REAL NOT NULL,
    monsoon_rh REAL NOT NULL,
    winter_temp REAL NOT NULL,
    winter_rh REAL NOT NULL,
    humidity_stress_factor REAL NOT NULL -- Baseline multiplier
);

-- 5. Routes Table
CREATE TABLE routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    distance_km INTEGER NOT NULL,
    typical_days INTEGER NOT NULL,
    ambient_stress_level TEXT NOT NULL, -- Moderate, High, Severe
    risk_factors TEXT
);

-- 6. Analyses Table
CREATE TABLE analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    mode TEXT NOT NULL, -- farmer, industry
    food_name TEXT NOT NULL,
    condition TEXT NOT NULL,
    storage_duration INTEGER NOT NULL,
    storage_type TEXT NOT NULL, -- Ambient, Refrigerated, Cold Storage
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    transport_mode TEXT NOT NULL,
    transit_days INTEGER NOT NULL,
    season TEXT NOT NULL,
    storage_temp REAL,
    relative_humidity REAL,
    -- Industry mode specific parameters
    initial_moisture REAL,
    free_fat REAL,
    target_gas TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- 7. Recommendations Table
CREATE TABLE recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    analysis_id INTEGER NOT NULL UNIQUE,
    primary_material TEXT NOT NULL,
    material_configuration TEXT NOT NULL,
    optimized_gauge TEXT NOT NULL,
    packaging_type TEXT NOT NULL,
    otr_target REAL NOT NULL,
    wvtr_target REAL NOT NULL,
    map_o2 REAL NOT NULL,
    map_co2 REAL NOT NULL,
    map_n2 REAL NOT NULL,
    bio_alternative_1 TEXT,
    bio_alternative_2 TEXT,
    shelf_life_original INTEGER NOT NULL,
    shelf_life_extended INTEGER NOT NULL,
    shelf_life_extension_pct INTEGER NOT NULL,
    sustainability_score REAL NOT NULL,
    unit_cost_inr REAL NOT NULL,
    plastic_reduction_pct INTEGER NOT NULL,
    carbon_impact TEXT NOT NULL,
    climate_stress_score INTEGER NOT NULL,
    humidity_risk_score INTEGER NOT NULL,
    temperature_risk_score INTEGER NOT NULL,
    transit_risk_score INTEGER NOT NULL,
    smart_insight TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(analysis_id) REFERENCES analyses(id) ON DELETE CASCADE
);

-- 8. PackAudit Results Table
CREATE TABLE packaudit_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    analysis_id INTEGER,
    image_filename TEXT NOT NULL,
    opacity_pct REAL NOT NULL,
    reflectivity_pct REAL NOT NULL,
    detected_type TEXT NOT NULL,
    seal_integrity TEXT NOT NULL,
    vulnerability_score INTEGER NOT NULL, -- 1-10
    vulnerability_reason TEXT NOT NULL,
    recommended_upgrade TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(analysis_id) REFERENCES analyses(id) ON DELETE SET NULL
);

-- 9. Translations Table
CREATE TABLE translations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lang TEXT NOT NULL, -- en, hi, mr
    trans_key TEXT NOT NULL,
    trans_value TEXT NOT NULL,
    UNIQUE(lang, trans_key)
);
