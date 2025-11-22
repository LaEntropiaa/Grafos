from grafos import *
from grafos.grafo import benchmark

for nodes in range(10, 101, 10):
    for p in range(5, 51, 5):
        name = f"results/{nodes}_{p}.csv"
        benchmark(1000, nodes, 1, 10, p, name)

