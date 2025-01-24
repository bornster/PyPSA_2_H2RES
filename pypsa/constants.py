DEFAULT_EPSG = 4326
DEFAULT_TIMESTAMP = "now"
ENERGY_SOURCES = {
    "Hydro": {
        "technology": ["HDAM", "HPHS", "HROR"],
        "final_life_cap": 1,
        "life_time": 100,
        "max_growth": 500,
        "ramping_cost": 0,
        "co2_emissions": 0,
    },
    "Biomass": {
        "technology": ["ICEN", "GTUR", "STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 0.5,
        "co2_emissions": 0,
    },
    "Coal": {
        "technology": ["STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 1.8,
        "co2_emissions": 1.1,
    },
    "Gas": {
        "technology": ["STUR", "COMC", "GTUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 0.5,
        "co2_emissions": 0.4,
    },
    "Oil": {
        "technology": ["STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 1.8,
        "co2_emissions": 0.5,
    },
    "Nuclear": {
        "technology": ["STUR"],
        "final_life_cap": 0,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 1.8,
        "co2_emissions": 0,
    },
    "Solar": {
        "technology": ["PHOT"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 4000,
        "ramping_cost": 0,
        "co2_emissions": 0,
    },
    "Wind": {
        "technology": ["WTON"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 2000,
        "ramping_cost": 0,
        "co2_emissions": 0,
    }
}
