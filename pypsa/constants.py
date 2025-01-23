DEFAULT_EPSG = 4326
DEFAULT_TIMESTAMP = "now"
ENERGY_SOURCES = {
    "Hydro": {
        "technology": ["HDAM", "HPHS", "HROR"],
        "final_life_cap": 1,
        "life_time": 100,
        "max_inv_period": 500,
    },
    "Biomass": {
        "technology": ["ICEN", "GTUR", "STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_inv_period": 100,
    },
    "Coal": {
        "technology": ["STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_inv_period": 100,
    },
    "Gas": {
        "technology": ["STUR", "COMC", "GTUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_inv_period": 100,
    },
    "Oil": {
        "technology": ["STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_inv_period": 100,
    },
    "Nuclear": {
        "technology": ["STUR"],
        "final_life_cap": 0,
        "life_time": 20,
        "max_inv_period": 100,
    },
    "Solar": {
        "technology": ["PHOT"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_inv_period": 4000,
    },
    "Wind": {
        "technology": ["WTON"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_inv_period": 2000,
    }
}
