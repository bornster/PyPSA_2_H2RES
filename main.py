import pypsa

n = pypsa.Network()
#n = pypsa.examples.ac_dc_meshed()
#n = pypsa.examples.scigrid_de()
#n = pypsa.examples.storage_hvdc()

n.export_to_xml_folder("xml_test_folder")