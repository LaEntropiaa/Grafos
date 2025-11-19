from grafos import *

grafo = Graph.random_graph(20, 10, 1, 10);

distance, route = grafo.floydWarshall("0", "6")
print(distance)
print(route)

