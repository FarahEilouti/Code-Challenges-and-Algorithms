# Write your test here
import pytest
from challenge03 import Tree

def test_convert_to_BST():

    tree = Tree()
    array = [5, 6, 4 , 3]
    tree.convert_to_BST(array)

    actual = tree.pre_order_array
    expected = [5, 4, 3, 6]
    assert actual == expected
    
def test_convert_to_BST2():

    tree = Tree()
    array = [4 , 3]
    tree.convert_to_BST(array)

    actual = tree.pre_order_array
    expected = [4, 3]
    assert actual == expected 