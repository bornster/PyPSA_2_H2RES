| **H2RES variables**            | **PyPSA alternatives**       |
|-----------------------------|-----------------------------------------------|
| genco_data["unit_name"]                   | network.generators["name"]      |
| genco_data["cap_mw"]| network.generators["p_nom"]|
|genco_data["fuel_type"]|network.generators["carrier"]|
|genco_data["decom_start_existing_cap"]||