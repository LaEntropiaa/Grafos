from .grafo import Graph
from grafos import grafo

def test_dijkstra_1():
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

    assert distance == 19
    assert route == ["0", "1", "3", "4", "6"]

def test_dijkstra_2():
    grafo = Graph(directed=True)

    grafo.add_node("0");
    grafo.add_node("1");
    grafo.add_node("2");
    grafo.add_node("3");
    grafo.add_node("4");

 
    grafo.connect_nodes("0", "1", 3);
    grafo.connect_nodes("0", "3", 7);
    grafo.connect_nodes("0", "4", 8);
    grafo.connect_nodes("4", "3", 3);
    grafo.connect_nodes("1", "3", 4);
    grafo.connect_nodes("1", "2", 1);
    grafo.connect_nodes("3", "2", 2);

    distance, route = grafo.dijkstra("0", "2")
    assert distance == 4
    assert route == ["0", "1", "2"]

def test_dijkstra_3():
    grafo = Graph();

    grafo.add_node("0")
    grafo.add_node("1")

    grafo.connect_nodes("0", "1", 3);

    distancia, route = grafo.dijkstra("0", "1")
    assert distancia == 3
    assert route == ["0", "1"]    
