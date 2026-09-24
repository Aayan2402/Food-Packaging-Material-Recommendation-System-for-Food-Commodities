"""
PackSense AI - Channel C: India Logistics & Climate Stress Engine
Calculates dynamic route stress, humidity multipliers, and barrier recalibrations
based on origin-destination transit through Indian agro-climatic zones.
"""

from ai.knowledge_base import get_climate_for_city

def calculate_climate_stress(origin, destination, transport_mode, transit_days, season, manual_temp=None, manual_rh=None):
    """
    Computes real-time logistics and climatic stress indices for highway transit across India.
    
    Parameters:
      origin (str): e.g., 'Pune'
      destination (str): e.g., 'Chennai'
      transport_mode (str): 'Ambient Open Truck', 'Refrigerated Truck', 'Certified Cold Chain', 'Rail Transport'
      transit_days (int): duration on highways (e.g., 4)
      season (str): 'Summer', 'Monsoon', 'Winter'
      manual_temp (float): optional user manual temp in Industry mode
      manual_rh (float): optional user manual RH in Industry mode
      
    Returns:
      dict with scores, risk factors, and dynamic barrier adjustments.
    """
    orig_clim = get_climate_for_city(origin)
    dest_clim = get_climate_for_city(destination)
    
    # 1. Determine active ambient conditions based on season
    season_key = season.lower() if season else "monsoon"
    if "summer" in season_key:
        t_orig, rh_orig = orig_clim["summer_temp"], orig_clim["summer_rh"]
        t_dest, rh_dest = dest_clim["summer_temp"], dest_clim["summer_rh"]
    elif "winter" in season_key:
        t_orig, rh_orig = orig_clim["winter_temp"], orig_clim["winter_rh"]
        t_dest, rh_dest = dest_clim["winter_temp"], dest_clim["winter_rh"]
    else:  # monsoon
        t_orig, rh_orig = orig_clim["monsoon_temp"], orig_clim["monsoon_rh"]
        t_dest, rh_dest = dest_clim["monsoon_temp"], dest_clim["monsoon_rh"]

    # Use manual overrides if provided
    avg_temp = manual_temp if (manual_temp is not None and manual_temp > 0) else ((t_orig + t_dest) / 2.0)
    avg_rh = manual_rh if (manual_rh is not None and manual_rh > 0) else ((rh_orig + rh_dest) / 2.0)

    # 2. Temperature Risk Score (0 - 100)
    # Severe risk when ambient heat exceeds 32°C without cold chain
    if "cold chain" in transport_mode.lower():
        temp_risk = 15
    elif "refrigerated" in transport_mode.lower():
        temp_risk = 28
    else:
        # Open truck or rail - exposed to thermal gradients
        if avg_temp >= 40:
            temp_risk = 92
        elif avg_temp >= 35:
            temp_risk = 80
        elif avg_temp >= 30:
            temp_risk = 65
        elif avg_temp >= 20:
            temp_risk = 40
        else:
            temp_risk = 25

    # 3. Humidity Risk Score (0 - 100)
    # Coastal corridors (like Chennai/Mumbai) experience extreme vapor pressure gradients
    max_rh = max(rh_orig, rh_dest)
    dest_stress_mult = dest_clim.get("humidity_stress_factor", 1.2)
    
    if max_rh >= 85 or dest_stress_mult >= 1.6:
        humidity_risk = 90
    elif max_rh >= 75:
        humidity_risk = 75
    elif max_rh >= 60:
        humidity_risk = 55
    else:
        humidity_risk = 35

    # Special coastal monsoon penalty
    if ("chennai" in destination.lower() or "mumbai" in destination.lower() or "kolkata" in destination.lower()) and "monsoon" in season_key:
        humidity_risk = min(98, humidity_risk + 10)

    # 4. Transit Duration Risk Score (0 - 100)
    # Longer road journeys amplify vibration and barrier fatigue
    days = max(1, int(transit_days or 3))
    if days >= 6:
        transit_risk = 85
    elif days >= 4:
        transit_risk = 72
    elif days >= 2:
        transit_risk = 50
    else:
        transit_risk = 30

    if "rail" in transport_mode.lower():
        transit_risk = min(90, transit_risk + 8)  # Shunting shocks and depot delays

    # 5. Composite Climate Stress Score (0 - 100)
    weights = {"temp": 0.35, "rh": 0.40, "transit": 0.25}
    if "cold chain" in transport_mode.lower() or "refrigerated" in transport_mode.lower():
        weights = {"temp": 0.15, "rh": 0.50, "transit": 0.35}

    climate_stress = int((temp_risk * weights["temp"]) + (humidity_risk * weights["rh"]) + (transit_risk * weights["transit"]))
    climate_stress = max(15, min(98, climate_stress))

    # 6. Barrier Recalibration Multipliers
    # High humidity routes demand lower WVTR (tighter moisture barrier)
    # High thermal stress demands tighter oxygen barrier or down-gauge protection
    moisture_barrier_multiplier = 1.0
    if humidity_risk >= 80:
        moisture_barrier_multiplier = 0.55  # Needs 45% tighter WVTR threshold
    elif humidity_risk >= 65:
        moisture_barrier_multiplier = 0.75
        
    oxygen_barrier_multiplier = 1.0
    if temp_risk >= 75:
        oxygen_barrier_multiplier = 0.70  # Higher temperatures accelerate oxidation

    route_summary = f"{origin} → {destination} via {transport_mode} ({days} days, {season})"
    
    return {
        "origin": origin,
        "destination": destination,
        "transport_mode": transport_mode,
        "transit_days": days,
        "season": season,
        "avg_temp": round(avg_temp, 1),
        "avg_rh": round(avg_rh, 1),
        "temp_risk": temp_risk,
        "humidity_risk": humidity_risk,
        "transit_risk": transit_risk,
        "climate_stress": climate_stress,
        "moisture_barrier_multiplier": moisture_barrier_multiplier,
        "oxygen_barrier_multiplier": oxygen_barrier_multiplier,
        "route_summary": route_summary,
        "origin_clim": orig_clim,
        "dest_clim": dest_clim
    }
