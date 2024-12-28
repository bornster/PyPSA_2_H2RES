import pypsa

network = pypsa.Network()
n_buses = 3

for i in range(n_buses):
    network.add("Bus", "My bus {}".format(i),  v_nom=20.)

network.export_to_xml_folder()