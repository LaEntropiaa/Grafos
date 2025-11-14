from grafos import *

grafo = Graph()
grafo.add_node("0")
grafo.add_node("1")
grafo.add_node("2")
grafo.add_node("3")
grafo.add_node("4")
grafo.add_node("5")
grafo.add_node("6")


grafo.connect_nodes("0", "2", 6);
grafo.connect_nodes("0", "1", 2);
grafo.connect_nodes("2", "3", 8);
grafo.connect_nodes("1", "3", 5);
grafo.connect_nodes("3", "4", 10);
grafo.connect_nodes("3", "5", 15);
grafo.connect_nodes("4", "6", 2);
grafo.connect_nodes("5", "6", 6);

distance, route = grafo.dijkstra("0", "6")
print(distance)
print(route)

