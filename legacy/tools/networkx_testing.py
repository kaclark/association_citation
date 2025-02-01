import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("Abhinvagupta", "Spandakarika")
G.add_edge("Abhinvagupta", "Locana")
G.add_edge("Abhinvagupta", "Lacan")
G.add_edge("Lacan", "Freud")
G.add_edge("Freud", "Schopenhauer")
G.add_edge("Brentano", "Freud")
G.add_edge("Brentano", "Husserl")
G.add_edge("Kant", "Brentano")
G.add_edge("Kant", "Schopenhauer")
G.add_edge("Husserl", "Derrida")

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
print(nx.tutte_polynomial(G))
