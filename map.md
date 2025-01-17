| **H2RES variables**            | **PyPSA alternatives**       | **default values** |
|-----------------------------|-----------------------------------------------|----------------|
| genco_data["unit_name"]                   | network.generators["name"]      | none |
| genco_data["cap_mw"]| network.generators["p_nom"]| 0|
|genco_data["fuel_type"]|network.generators["carrier"]|""|
|genco_data["decom_start_existing_cap"]|  network.generators["lifetime"] - 10 | 0|
|genco_data["lifetime"]|network.generators["lifetime"]| infinity|
|genco_data["decom_start_new"]| network.generators["lifetime"] - 5|0|
|genco_data["final_life_cap"]| genco_data["fuel_type"] [0.2, 1,0]|0|
|genco_data["max_inv_period"]|TBD|TBD|
|genco_data["cap_factor"]|TBD - for now set as 1|1|
|genco_data["efficiency"]|network.generators["efficiency"]|1|
|genco_data["cost_no_fuel"]| TBD - for now set as 0|0|
|genco_data["cap_inv_cost"]|network.generators["capital_cost"]|0|
|genco_data["RampingCost"]|TBD - network.generators["ramp_limit_up/ramp_limit_down"]|TBD|
|genco_data["CO2Intensity"]|TBD - genco_data["fuel_type"] & genco_data["efficiency"]|TBD|
|genco_data["technology"]|Additional attribute created|NaN|
|genco_data["RampUpRate"]|TBD - network.generators["ramp_limit_up"] while snapshot time = 1h|NaN|
|genco_data["RampDownRate"]|TBD - network.generators["ramp_limit_down"] while snapshot time = 1h|NaN|
|genco_data["PrimaryReserve"]|NaN|NaN|
|genco_data["SecondaryReserve"]|NaN|NaN|
|genco_data["Stab_factor"]|1|1|
|genco_data["CHPType"]|TBD|TBD|
|genco_data["STOCapacity"]|network.storage_unit["p_nom"] * network.storage_unit["max_hours"]|0|
|genco_data["STOSelfDischarge"]|network.storage_unit["inflow"]|0|
|genco_data["STOMaxChargingPower"]|network.storage_unit["p_store"]|0|
|genco_data["STOChargingEfficiency"]|network.storage["efficiency_store"]|1|
|genco_data["CHPPowerToHeat"]|TBD|TBD|
|genco_data["CHPPowerLossFactor"]|TBD|TBD|
|genco_data["CHPMaxHeat"]|network.storage_unit["p_nom"]|0|


demand_2020_2050 pogledat preko snapshota i izracunat power po satu kroz godinu