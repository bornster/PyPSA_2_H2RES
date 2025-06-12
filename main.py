import pypsa

n = pypsa.Network('/Users/borna_radosevic/Downloads/test/networks/base_s_128_elec_.nc')
#n = pypsa.examples.ac_dc_meshed()
#n = pypsa.examples.scigrid_de()
#n = pypsa.examples.storage_hvdc()
n.export_to_h2res("h2res_test_folder")