from __future__ import annotations
from types import new_class
from .nodo import Node
import heapq
import random
import time
import csv

class Graph:
    def __init__(self, directed=False) -> None:
        self.nodes = {}
        self.directed = directed
        self.negative = False

    @staticmethod
    def random_graph(n: int, p: float, minw:int, maxw:int) -> Graph:
        new_graph = Graph()
        for i in range(n):
            new_graph.add_node(str(i))
        nodes = list(new_graph.nodes.keys())
        for i in range(1, len(nodes)):
            a = nodes[i]
            b = nodes[random.randint(0, i -1)]
            new_graph.connect_nodes(a, b, random.randint(minw, maxw))
        for n in nodes:
            for m in nodes:
                if n == m:
                    continue
                if random.randint(1, 100) < p:
                    new_graph.connect_nodes(n, m, random.randint(minw, maxw))
        return new_graph

    def add_node(self, id:str):
        if id not in self.nodes:
            self.nodes[id] = Node(id)

    def connect_nodes(self, node1_id:str, node2_id:str, weight:int) -> None:
        if node1_id not in self.nodes:
            self.add_node(node1_id)
        if node2_id not in self.nodes:
            self.add_node(node2_id)

        if weight < 0:
            self.negative = True
        # Basicamente accedemos al valor que guarda el diccioneario de nodos
        # y le añadimos un id y peso, ya con eso al acceder a un nodo podemos
        # usar la id guardada para acceder desde el grafo
        self.nodes[node1_id].add_neighbor(self.nodes[node2_id], weight)
        # Si no esta direccionado quiere decir que el mismo camino de un nodos
        # a otro es lo mismo y siempre existe entonces hay que conectar ambos
        # nodos bajo el mismo peso
        if not self.directed:
            self.nodes[node2_id].add_neighbor(self.nodes[node1_id], weight)

    def dijkstra(self, node1_id:str, node2_id:str, fast:bool = False) :
        distances = {n: float('inf') for n in self.nodes};
        distances[node1_id] = 0;

        previous = {n: None for n in self.nodes}
        heap = [(0, node1_id)]

        while heap:
            actual_distance, current_node_id = heapq.heappop(heap)
            if current_node_id == node2_id:
                break
            if actual_distance > distances[current_node_id]:
                continue

            node = self.nodes[current_node_id]
            for neighbour_id, weight in node.neighbors.items():
                new_distance = actual_distance + weight
                if new_distance < distances[neighbour_id]:
                    distances[neighbour_id] = new_distance
                    previous[neighbour_id] = current_node_id
                    heapq.heappush(heap, (new_distance, neighbour_id))
        if fast == True:
            return distances[node2_id]
        route = []
        n = node2_id
        while n is not None:
            route.append(n)
            n = previous[n]
        route.reverse()

        return distances[node2_id], route

    def floydWarshall(self, node1_id, node2_id, fast:bool = False):
        nodes = list(self.nodes.keys())
        n = len(nodes)

        distances = {i: dict.fromkeys(nodes, float('inf')) for i in nodes}
        next_node = {i: dict.fromkeys(nodes, None) for i in nodes}

        for i in nodes:
            distances[i][i] = 0

        for i in nodes:
            for neighbor, weight in self.nodes[i].neighbors.items():
                distances[i][neighbor] = weight
                next_node[i][neighbor] = neighbor
        for i in nodes:
            for j in nodes:
                for k in nodes:
                    if distances[j][i] + distances[i][k] < distances[j][k]:
                        distances[j][k] = distances[j][i] + distances[i][k]
                        next_node[j][k] = next_node[j][i]
        if fast == True:
            return distances[node1_id][node2_id]

        if next_node[node1_id][node2_id] is None:
            return float('inf'), None
        route = [node1_id]
        current = node1_id

        while current != node2_id:
            current = next_node[current][node2_id]
            route.append(current)

        return distances[node1_id][node2_id], route

    def edge_count(self):
        total = sum(len(node.neighbors) for node in self.nodes.values())
        return total // 2 if not self.directed else total

    def density(self):
        n = len(self.nodes)
        m = self.edge_count()
        return (2 * m) / (n * (n - 1)) if n > 1 else 0

    def __str__(self) -> str:
        string = ""
        for i in self.nodes.values():
            string += f"{i}\n"
        return string

def benchmark(n:int, nodes:int, minw:int, maxw:int, p:float, out:str): 
    with open(out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["exp", "source", "target", "edges", "density", "t_dijkstra", "t_floyd"])

        for i in range(n):
            g = Graph.random_graph(nodes, p, minw, maxw)

            src = str(random.randint(0, nodes - 1))
            dst = str(random.randint(0, nodes - 1))

            edges = g.edge_count()
            density = g.density()

            t0 = time.perf_counter()
            g.dijkstra(src, dst, True)  
            t1 = time.perf_counter()
            t_dijkstra = t1 - t0

            t0 = time.perf_counter()
            g.floydWarshall(src, dst, True)
            t1 = time.perf_counter()
            t_floyd = t1 - t0
            
            writer.writerow([i, src, dst, edges, density, t_dijkstra, t_floyd])
