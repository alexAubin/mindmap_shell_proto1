import networkx as nx
import matplotlib.pyplot as plt
from dbus import SessionBus

session_bus = SessionBus()


graph1 = nex.watts_strogatz_graph(30,3,0.1)



graph2 = nx.Graph()
graph2.add_nodes_from([1,2,3,4,5], name='nom')
graph2.add_edges_from([(1,2),(1,3,{'a':'trololo'}),(3,4),(3,5)])

graph = graph1

nx.draw_graphviz(graph)
nx.write_dot(graph, 'file.dot')
