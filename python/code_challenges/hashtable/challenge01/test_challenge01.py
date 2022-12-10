# Write your test here
import pytest
from challenge01 import Tree, Node

def test_hash_BST():
    tree=Tree()
    node1=Node(7)
    node2=Node(2)
    node3=Node(9)
    node4=Node(1)
    node5=Node(5)
    node6=Node(14)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    #node3.left = None
    node3.right = node6

    tree.root=node1
    # tree.findTarget(3)

    result = tree.findTarget(3)

    actual = result
    expected = True
    assert actual == expected

def test_hash_BST2():

    tree2=Tree()
    node1=Node(7)
    node2=Node(2)
    node3=Node(9)
    node4=Node(1)
    node5=Node(5)
    node6=Node(14)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    #node3.left = None
    node3.right = node6

    tree2.root=node1
    # tree.findTarget(3)

    result = tree2.findTarget(4)

    actual = result
    expected = False
    assert actual == expected