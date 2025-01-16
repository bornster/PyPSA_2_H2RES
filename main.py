import pypsa

n = pypsa.Network('examples/ac-dc-meshed/ac-dc-data')
#n = pypsa.examples.ac_dc_meshed()
#n = pypsa.examples.scigrid_de()
#n = pypsa.examples.storage_hvdc()
n.export_to_h2res("h2res_test_folder")