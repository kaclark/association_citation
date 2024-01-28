from tools import *

x_tattvas = read_map_list("data/tattvas.csv")
#print_mappings(x_tattvas)
#test = graph_from_map(x_tattvas[2], [("name", "sanskrit")], "tattvas")
#save_graph(test, "data/test_diag.png")
test2 = graph_from_list_of_maps(x_tattvas, [("term_name", "sanskrit"), ("category","term_name")], [("tattvas", "category")])
save_graph(test2, "data/test2_diag.png")
