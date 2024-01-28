import networkx as nx
import matplotlib.pyplot as plt

def read_csv(fd):
    with open(fd, "r") as fn:
        lines = [ll.split(",") for ll in [l.split('\n')[0] for l in fn.readlines()]]
    return lines

def bind_header_as_map(csv_lines):
    key_vector = csv_lines[0]
    codom_vectors = csv_lines[1:]
    c_maps = []
    for codom in codom_vectors:
        c_map = {}
        for ind, elt in enumerate(codom):
            c_map[key_vector[ind]] = elt
        c_maps.append(c_map)
    return c_maps

def read_map_list(fd):
    list_of_lists = read_csv(fd)
    return bind_header_as_map(list_of_lists)

def print_mappings(list_of_maps):
    for xi_map in list_of_maps:
        for k,v in xi_map.items():
            print(k,":",v)
        print("\n")

def graph_from_map(xi_map, relation_types, root_relations):
    #relation_types: tuples of pairs
    xi_graph = nx.Graph()
    for root_relation in root_relations:
        r_dom, r_codom = root_relation
        xi_graph.add_edge(r_dom, xi_map[r_codom])
    for relation_type in relation_types:
        dom, codom = relation_type
        xi_graph.add_edge(xi_map[dom], xi_map[codom])
    return xi_graph       

def save_graph(xi_graph, fd):
    nx.draw(xi_graph, with_labels=True, font_weight='bold')
    plt.savefig(fd)

def graph_from_list_of_maps(list_of_maps, relation_types, root_relation):
    x_graphs = [graph_from_map(xi_map, relation_types, root_relation) for xi_map in list_of_maps]
    x_graph = nx.Graph()
    for xg in x_graphs:
        x_graph.update(xg)
    return x_graph
