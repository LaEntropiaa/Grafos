from __future__ import annotations

class Node:
    def __init__(self, id:str) -> None:
        self.id = id
        self.neighbors = {}

    def add_neighbor(self, neighbor: Node, weight:int) -> None:
        self.neighbors[neighbor.id] = weight 
