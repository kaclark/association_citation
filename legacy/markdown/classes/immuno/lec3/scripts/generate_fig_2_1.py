import graphviz
import matplotlib.pyplot as plt
import networkx as nx

graph = graphviz.Digraph(format="png")
#graph.node_attr['fontsize'] = '20'
#Pathogens can be blocked by Barriers like Skin
n1 = "Pathogen"
graph.node(n1, shape="none", fontname="bold")
n2 = "Containment by an anatomic barrier"
graph.node(n2, shape="none", fontname="bold")
graph.edge(n1,n2)

#This prevents infection
n2b = "Prevention of infection"
graph.node(n2b, shape="none", fontname="bold")
graph.edge(n2, n2b, orientation="right")

#Upon Failure, Infection
n3 = "Infection"
graph.node(n3, shape="none", fontname="bold")
graph.edge(n2, n3, label="Fail")

#This leads to recognition by first line of defense
n4 = "Recognition by preformed nonspecific and broadly specific effectors"
n4a = "Removal of infectous agent"
graph.node(n4, shape="none", fontname="bold")
graph.node(n4a, shape="none", fontname="bold")
graph.edge(n3, n4)
graph.edge(n4, n4a)


#Upon Failure, recruitment of effector cells
n5 = "Recruitment of effector cells"
graph.node(n5, shape="none", fontname="bold", xlabel="4-96hrs")
graph.edge(n4, n5, label="Fail")
n6 = "Recognition of PAMPs, Activation of effector cells and inflammation"
graph.node(n6, shape="none", fontname="bold")
graph.edge(n5,n6)
graph.edge(n6, n4a)

n7 = "Transport of antigen to lymphoid organs"
graph.node(n7, shape="none", fontname="bold", xlabel=">96hrs")
graph.edge(n6, n7, label="Fail")
n8 = "Recognition by naive B and T cells"
graph.node(n8, shape="none", fontname="bold")
graph.edge(n7,n8)
n9 = "Clonal expansion and differentiation to effector cells"
graph.edge(n8,n9)
graph.node(n9, shape="none", fontname="bold")
graph.edge(n9, n4a)

#graph.view() # Save the flowchart as an image file
graph.render(filename="fig_2_1")
