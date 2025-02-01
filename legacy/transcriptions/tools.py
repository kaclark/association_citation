import networkx as nx
import matplotlib.pyplot as plt
from sympy import Matrix


#Samkyha transcription derived tools
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

def save_graph(xi_graph, fd, edgelabels=False):
    if edgelabels:
        pos = nx.spring_layout(xi_graph)
        edge_labels = dict([((n1, n2), f'{n3}') for n1, n2, n3 in xi_graph.edges(data=True)])
        nx.draw(xi_graph, pos, with_labels=True, node_color="#d2b48c")
        nx.draw_networkx_edge_labels(xi_graph, pos, edge_labels=edge_labels)
    else:
        nx.draw(xi_graph, with_labels=True, node_color="#d2b48c")
    plt.savefig(fd)

def graph_from_list_of_maps(list_of_maps, relation_types, root_relation):
    x_graphs = [graph_from_map(xi_map, relation_types, root_relation) for xi_map in list_of_maps]
    x_graph = nx.Graph()
    for xg in x_graphs:
        x_graph.update(xg)
    return x_graph

def graph_from_matrix():
    # Create a SymPy matrix
    sympy_matrix = Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

    # Convert the SymPy matrix to a list of lists
    matrix_as_list = sympy_matrix.tolist()

    # Flatten the list of lists
    edges = [(i, j) for i, row in enumerate(matrix_as_list) for j, value in enumerate(row) if value != 0]

    # Create a NetworkX graph using the list of edges
    G = nx.Graph(edges)
    return G

#Monadology Derived Tools
def read_first_line(fdo):
    return fdo.readlines()[0].split('\n')[0]

def add_func_subgraph(dom, codom, f, xi_graph):
    xi_graph.add_edge(dom, codom, function=f)
    return xi_graph

def add_func_subgraph_copied(dom, codom, f, xi_graph):
    xj_graph = nx.Graph()
    xj_graph.add_edge(dom, codom, function=f)
   
    #At this step, we should consider:
    #what if this is inefficient?
    #it seems functional though
    xw_graph = nx.Graph()
    xw_graph.update(xj_graph)
    xw_graph.update(xi_graph)
    return xw_graph

def get_func_subgraph(dom, codom, f):
    xj_graph = nx.Graph()
    xj_graph.add_edge(dom, codom, function=f)
    return xj_graph 
