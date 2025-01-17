DEFAULT_EPSG = 4326
DEFAULT_TIMESTAMP = "now"
ENERGY_SOURCES = {
    "Hydro": {
        "technology": ["HDAM", "HPHS", "HROR"],
        "final_life_cap": 1
    },
    "Biomass": {
        "technology": ["ICEN", "GTUR", "STUR"],
        "final_life_cap": 0.2
    },
    "Coal": {
        "technology": ["STUR"],
        "final_life_cap": 0.2
    },
    "Gas": {
        "technology": ["STUR", "COMC", "GTUR"],
        "final_life_cap": 0.2
    },
    "Oil": {
        "technology": ["STUR"],
        "final_life_cap": 0.2
    },
    "Nuclear": {
        "technology": ["STUR"],
        "final_life_cap": 0
    },
    "Solar": {
        "technology": ["PHOT"],
        "final_life_cap": 0.2
    },
    "Wind": {
        "technology": ["WTON"],
        "final_life_cap": 0.2
    }
}
