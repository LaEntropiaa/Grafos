from grafos import *

grafo = Graph()
grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")

grafo.connect_nodes("A", "B", 8);
grafo.connect_nodes("A", "C", 9);

print(grafo);
