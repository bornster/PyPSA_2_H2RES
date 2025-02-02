from typing import Any, Dict

DEFAULT_EPSG = 4326
DEFAULT_TIMESTAMP = "now"
DECOM_START_EXISTING_CAP_DEFAULT_VALUE: float = 10.0
DECOM_START_NEW_DEFAULT_VALUE: float = 5.0
STO_SELF_DISCHARGE_DEFAULT_VALUE: float = 0.01
STO_CHARGING_EFFICIENCY_DEFAULT_VALUE: float = 0.75
CHP_POWER_LOSS_FACTOR_DEFAULT_VALUE: float = 0.18
ENERGY_SOURCES : Dict[str, Dict[str, Any]]= {
    "Hydro": {
        "technology": ["HDAM", "HPHS", "HROR"],
        "final_life_cap": 1,
        "life_time": 100,
        "max_growth": 500,
        "ramping_cost": 0.0,
        "co2_emissions": 0.0,
    },
    "Biomass": {
        "technology": ["ICEN", "GTUR", "STUR"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 0.5,
        "co2_emissions": 0.0,
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
        "final_life_cap": 0.0,
        "life_time": 20,
        "max_growth": 100,
        "ramping_cost": 1.8,
        "co2_emissions": 0.0,
    },
    "Solar": {
        "technology": ["PHOT"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 4000,
        "ramping_cost": 0.0,
        "co2_emissions": 0.0,
    },
    "Wind": {
        "technology": ["WTON"],
        "final_life_cap": 0.2,
        "life_time": 20,
        "max_growth": 2000,
        "ramping_cost": 0.0,
        "co2_emissions": 0.0,
    }
}
