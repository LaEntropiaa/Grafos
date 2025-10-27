from .nodo import Node

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

    def __str__(self) -> str:
        string = ""
        for i in self.nodes.values():
            string += f"{i}\n"
        return string

