import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["A", "B", "C", "D", "E"])
G.add_edges_from([("A", "B"), ("A", "C"), ("C", "D"), ("B", "D"), ("D", "E")])
nx.draw(G, with_labels=True)
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print(num_nodes, num_edges, is_connected)
print(degree_centrality)
print(closeness_centrality)
print(betweenness_centrality)



