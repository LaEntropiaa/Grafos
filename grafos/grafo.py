from types import new_class
from .nodo import Node
import heapq

class Graph:
    def __init__(self, directed=False) -> None:
        self.nodes = {}
        self.directed = directed
        self.negative = False

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

    def dijkstra(self, node1_id:str, node2_id:str) :
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

        route = []
        n = node2_id
        while n is not None:
            route.append(n)
            n = previous[n]
        route.reverse()

        return distances[node2_id], route

    def __str__(self) -> str:
        string = ""
        for i in self.nodes.values():
            string += f"{i}\n"
        return string

