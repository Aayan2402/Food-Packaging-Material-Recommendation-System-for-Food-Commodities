-- PackSense AI - Seed Data
-- SIH Problem Statement 236: Standardized Food Science & Packaging Knowledge Base

-- ============================================================
-- 1. FOOD COMMODITIES (Biochemical Knowledge Base)
-- ============================================================
INSERT INTO foods (name, category, default_condition, respiration_rate, moisture_sensitivity, fat_vulnerability, ph, temp_sensitivity, microbial_risk, ethylene_emission, standard_shelf_life_days, target_otr, target_wvtr, opt_temp_c, opt_rh_pct, spoilage_mechanism, notes) VALUES
('Strawberry', 'Fruit', 'Fresh', 'High', 'High', 'Low', 3.5, 'Severe', 'Critical', 'Low', 4, 1800.0, 15.0, 2.0, 92.0,
 'High moisture transpiration + rapid respiration leading to mold (Botrytis cinerea), softness, and condensation rotting.',
 'Requires micro-perforated tray + anti-fog lidding film to balance O2/CO2 without suffocation or condensation.'),

('Mango', 'Fruit', 'Fresh', 'High', 'Medium', 'Low', 4.5, 'High', 'Moderate', 'High', 7, 2200.0, 18.0, 12.0, 88.0,
 'Climacteric fruit with peak ethylene surge, rapid starch-to-sugar conversion, skin shriveling and anthracnose rot.',
 'Needs semi-permeable breathable bio-film or LDPE with ethylene scrubbers to delay ripening.'),

('Apple', 'Fruit', 'Fresh', 'Medium', 'Medium', 'Low', 3.8, 'Moderate', 'Low', 'High', 20, 2500.0, 12.0, 4.0, 90.0,
 'Continuous ethylene emission and skin dehydration causing internal browning and moisture loss.',
 'Perforated polymeric wraps preserve crispness while venting respiration byproducts.'),

('Tomato', 'Vegetable', 'Fresh', 'Medium', 'High', 'Low', 4.3, 'High', 'Moderate', 'Medium', 6, 2000.0, 14.0, 11.0, 85.0,
 'Chilling injury below 10°C, high transpiration causing surface mold and water loss.',
 'Needs ventilated PET clamshell or moisture-buffering bio-film.'),

('Potato', 'Vegetable', 'Raw', 'Low', 'Low', 'Low', 6.0, 'Low', 'Low', 'None', 30, 3500.0, 25.0, 15.0, 80.0,
 'Exposure to visible and UV light triggers chlorophyll and poisonous solanine greening; excessive moisture causes sprouting and bacterial soft rot.',
 'Requires opaque or dark light-blocking micro-vented kraft paper or dark HDPE sacks.'),

('Potato Chips', 'Snack', 'Fried', 'None', 'Extreme', 'Extreme', 6.2, 'Low', 'Low', 'None', 14, 2.0, 1.0, 25.0, 50.0,
 'Lipid oxidation of free oils (high fat ~35%) caused by oxygen and UV light turns food rancid; hygroscopic starch absorbs moisture above 3% losing signature crunch.',
 'Mandates zero-light, extreme oxygen and moisture barrier (Metallized BOPP / Nitrogen-flushed MAP).'),

('Namkeen', 'Snack', 'Fried', 'None', 'Extreme', 'High', 6.4, 'Low', 'Low', 'None', 20, 5.0, 1.5, 25.0, 50.0,
 'Rancidity of deep-fried nuts and chickpea flour due to atmospheric oxygen; aromatic spice volatile loss and soggy texture.',
 'Requires multi-layer metallized barrier laminate with airtight heat seal.'),

('Paneer', 'Dairy', 'Fresh', 'None', 'Extreme', 'Low', 6.1, 'Critical', 'Critical', 'None', 3, 20.0, 4.0, 4.0, 90.0,
 'High water activity (aw > 0.98) and near-neutral pH trigger rampant psychrotrophic bacterial proliferation and fungal mold growth.',
 'Requires strict cold chain + vacuum pouch or active MAP (80% N2 / 20% CO2) high barrier film.'),

('Meat', 'Meat', 'Fresh', 'None', 'High', 'Medium', 5.6, 'Critical', 'Critical', 'None', 3, 10.0, 3.0, 1.0, 85.0,
 'Aerobic bacterial decay (Pseudomonas), myoglobin pigment oxidation turning red flesh brown, and lipid breakdown.',
 'Demands high-barrier EVOH/PET vacuum skin pack or MAP gas flushing with strict refrigeration.'),

('Other Produce', 'Vegetable', 'Fresh', 'High', 'High', 'Low', 5.5, 'High', 'Moderate', 'Low', 5, 2400.0, 16.0, 4.0, 90.0,
 'Transpiration water loss, wilting of green leaf tissue, rapid chlorophyll degradation and enzymatic browning.',
 'Requires high-breathability micro-perforated bio-film to prevent moisture pooling and anaerobic rot.');

-- ============================================================
-- 2. PACKAGING MATERIALS DATABASE (ASTM Specs & Indian Gauges)
-- ============================================================
INSERT INTO packaging_materials (material_name, material_type, ot_r, wvtr, thickness_micron, gauge, flexibility, transparency, moisture_barrier, oxygen_barrier, light_barrier, biodegradable, industrial_compost_only, estimated_cost_inr, sustainability_score, recommended_food, environmental_nuance, notes) VALUES
('PET', 'Conventional Plastic', 80.0, 30.0, 50, 200, 'Rigid', 'Crystal Clear', 'Medium', 'Medium', 'None', 0, 0, 1.20, 4.5,
 'Fresh berries, cut fruits, cherry tomatoes, pre-cut salads',
 'Widely recycled in India via mechanical recycling, but petroleum-based with high carbon footprint.',
 'Stiff, crystal-clear resin ideal for structural clamshells and clear punnets.'),

('LDPE', 'Conventional Plastic', 3200.0, 18.0, 40, 160, 'Highly Flexible', 'Semi-Transparent', 'Medium', 'Low', 'None', 0, 0, 0.65, 3.8,
 'Milk pouches, general grocery, low-respiration pulses',
 'Soft, stretchy film with high breathability. Prone to microplastic littering if not recycled.',
 'Standard economical pouch material across Indian local markets.'),

('HDPE', 'Conventional Plastic', 1500.0, 8.0, 35, 140, 'Semi-Rigid', 'Semi-Transparent', 'High', 'Medium', 'Moderate', 0, 0, 0.85, 4.0,
 'Bulk produce liners, dry food containers, grain sacks',
 'High tensile strength, crinkly feel, very low moisture transmission.',
 'Excellent moisture protection for dry products; moderate gas barrier.'),

('Metallized BOPP', 'Multi-layer Foil', 2.5, 0.8, 25, 100, 'Flexible', 'Opaque', 'Exceptional', 'Exceptional', 'Complete', 0, 0, 1.45, 3.0,
 'Potato chips, namkeen, fried snacks, roasted nuts, coffee',
 'Difficult to recycle due to aluminum-plastic multi-material fusion, but provides unrivaled shelf-life for oxygen/light sensitive snacks.',
 'The shiny silver interior is an aluminum vacuum-coated layer that completely blocks light, air, and moisture.'),

('PLA', 'Biopolymer', 450.0, 42.0, 45, 180, 'Rigid', 'Crystal Clear', 'Low', 'Medium', 'None', 1, 1, 2.10, 8.6,
 'Strawberries, high-end organic berries, fresh fruit trays',
 'Bio-based from corn/cassava starch. Decomposes within 90 days in INDUSTRIAL composting facilities (requires >58°C and specific humidity); will not degrade quickly in home compost.',
 'Crystal clear green alternative to PET; excellent rigidity and consumer appeal.'),

('Cellulose / Chitosan', 'Biopolymer', 90.0, 26.0, 30, 120, 'Flexible', 'Semi-Transparent', 'Medium', 'High', 'Moderate', 1, 0, 2.75, 9.4,
 'Bakery items, semi-dry cheeses, dried fruits, premium cookies',
 'Extracted from forestry cellulose and seafood processing waste (chitin). Marine and home compostable; naturally inhibits mold and bacteria.',
 'Natural antimicrobial properties and high grease resistance without synthetic fluorochemical coatings.'),

('PBAT', 'Biopolymer', 950.0, 32.0, 38, 152, 'Highly Flexible', 'Semi-Transparent', 'Medium', 'Low', 'None', 1, 0, 2.40, 8.9,
 'Fresh vegetables, leafy greens, pulses, short-transit fresh produce',
 'Biodegradable random copolymer; fully breaks down in agricultural soil and home compost without leaving persistent microplastics.',
 'Flexible and tough, mimics LDPE elasticity while supporting green agricultural sustainability.'),

('PHA', 'Biopolymer', 700.0, 20.0, 35, 140, 'Flexible', 'Semi-Transparent', 'High', 'Medium', 'Moderate', 1, 0, 3.10, 9.5,
 'Organic snacks, fresh produce, perishables',
 'Naturally synthesized by bacterial fermentation of plant sugars or waste oils. 100% marine degradable and ocean safe.',
 'Premium bio-polymer with the highest environmental integrity; expanding commercial availability in India.');

-- ============================================================
-- 3. INDIAN CLIMATE DATA (Seasonal Climatology & Humidity Multipliers)
-- ============================================================
INSERT INTO climate_data (city, state, zone, summer_temp, summer_rh, monsoon_temp, monsoon_rh, winter_temp, winter_rh, humidity_stress_factor) VALUES
('Pune', 'Maharashtra', 'Western Plateau', 36.0, 48.0, 26.0, 82.0, 28.0, 42.0, 1.15),
('Chennai', 'Tamil Nadu', 'Coromandel Coast', 39.0, 78.0, 32.0, 89.0, 29.0, 76.0, 1.65),
('Mumbai', 'Maharashtra', 'Konkan Coast', 35.0, 75.0, 29.0, 92.0, 30.0, 68.0, 1.70),
('Delhi', 'Delhi NCR', 'Northern Plains', 42.0, 40.0, 33.0, 79.0, 18.0, 65.0, 1.30),
('Bengaluru', 'Karnataka', 'Deccan Plateau', 34.0, 52.0, 25.0, 78.0, 27.0, 55.0, 1.10),
('Hyderabad', 'Telangana', 'Central Plateau', 40.0, 45.0, 28.0, 76.0, 28.0, 50.0, 1.20),
('Kolkata', 'West Bengal', 'Eastern Delta', 37.0, 74.0, 30.0, 88.0, 25.0, 66.0, 1.60),
('Nagpur', 'Maharashtra', 'Vidarbha Interior', 44.0, 32.0, 28.0, 81.0, 27.0, 46.0, 1.25),
('Ahmedabad', 'Gujarat', 'Western Arid', 43.0, 42.0, 31.0, 80.0, 28.0, 45.0, 1.22),
('Shimla', 'Himachal Pradesh', 'Himalayan High', 24.0, 55.0, 19.0, 88.0, 11.0, 60.0, 1.05);

-- ============================================================
-- 4. INTER-CITY LOGISTICS ROUTES
-- ============================================================
INSERT INTO routes (origin, destination, distance_km, typical_days, ambient_stress_level, risk_factors) VALUES
('Pune', 'Chennai', 1180, 4, 'Severe', 'Transits from dry western plateau to extreme saline coastal humidity (89% RH in monsoon); intense moisture ingress risk for crisps & rapid berry mold.'),
('Pune', 'Mumbai', 150, 1, 'High', 'Rapid elevation drop into severe coastal humidity; condensation shock for cold-stored produce.'),
('Delhi', 'Mumbai', 1420, 4, 'Severe', 'Crosses northern dry heat waves into saturated coastal marine moisture.'),
('Bengaluru', 'Chennai', 350, 2, 'High', 'Moderate plateau climate to heavy coastal heat and marine humidity.'),
('Nagpur', 'Kolkata', 1050, 3, 'High', 'Intense inland central heat shifting to high humidity delta conditions.');

-- ============================================================
-- 5. SAMPLE DEFAULT USERS (Password: demo123)
-- ============================================================
INSERT INTO users (name, email, password_hash, role, language, mode) VALUES
('PackSense Demo User', 'demo@packsense.ai', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'farmer', 'en', 'farmer'),
('Demo Farmer', 'farmer@packsense.ai', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'farmer', 'en', 'farmer'),
('Packaging Scientist', 'lab@packsense.ai', 'd3ad9315b7be5dd53b31a273b3b3aba5defe700808305aa16a3062b76658a791', 'industry', 'en', 'industry');
