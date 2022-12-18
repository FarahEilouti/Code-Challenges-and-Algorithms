# Write your test here

import pytest
from challenge01 import Graph, bfsOfGraph


def test_bfsOfGraph():
    graph = Graph()
    
    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")
    e = graph.add_node("E")
    f = graph.add_node("F")
    
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(d, f)
    
    expected = ["A", "B", "C", "D", "E", "F"]
    actual = bfsOfGraph(graph, "A")
    assert expected == actual