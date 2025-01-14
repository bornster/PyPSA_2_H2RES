| **H2RES variables**            | **PyPSA alternatives**       |
|-----------------------------|-----------------------------------------------|
| genco_data["unit_name"]                   | network.generators["name"]      |
| genco_data["cap_mw"]| network.generators["p_nom"]|
|genco_data["fuel_type"]|network.generators["carrier"]|
|genco_data["decom_start_existing_cap"]| default value 15 years (map together with life time) |
|genco_data["lifetime"]|network.generators["lifetime"]|
|genco_data["decom_start_new"]| decom_start_new < network.generators["lifetime"] |
|genco_data["final_life_cap"]|map to the genco_data["fuel_type"]|
|genco_data["max_inv_period"]|TBD|
|genco_data["cap_factor"]|default 1|
|genco_data["efficiency"]|network.generators["efficiency"]||
|genco_data["cost_no_fuel"]|default 0|
|genco_data["cap_inv_cost"]|network.generators["capital_cost"]|
|genco_data["RampingCost"]|network.generators["mu_ramp_limit_up/mu_ramp_limit_down"]|
|genco_data["CO2Intensity"]|TBD with the genco_data["fuel_type"] & genco_data["efficiency"]|
|genco_data["technology"]|TBD possible change to the object structure of generator|
|genco_data["RampUpRate"]|network.generators["ramp_limit_up"] while snapshot time = 1h|
|genco_data["RampDownRate"]|network.generators["ramp_limit_down"] while snapshot time = 1h|
|genco_data["PrimaryReserve"]|NaN default|
|genco_data["SecondaryReserve"]|NaN default|
|genco_data["Stab_factor"]|1 default for now|
|genco_data["CHPType"]|TBD|
|genco_data["STOCapacity"]|network.storage_unit["p_nom"] * network.storage_unit["max_hours"]|
|genco_data["STOSelfDischarge"]|network.storage_unit["inflow"]|
|genco_data["STOMaxChargingPower"]|network.storage_unit["p_store"]|
|genco_data["STOChargingEfficiency"]|network.storage["efficiency_store"]|
|genco_data["CHPPowerToHeat"]|TBD|
|genco_data["CHPPowerLossFactor"]|TBD|
|genco_data["CHPMaxHeat"]|network.storage_unit["p_nom"]|


demand_2020_2050 pogledat preko snapshota i izracunat power po satu kroz godinu