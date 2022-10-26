import pytest
from challenge02 import LinkedList

def test_linked_list():

    linkedList1 = LinkedList()

    linkedList1.append('a')
    linkedList1.append('b')
    linkedList1.append('c')
    linkedList1.append('d')
    linkedList1.append('e')

    result = linkedList1.middle_node()
    

    expected = ['c', 'd', 'e']
    actual = result
    assert actual == expected
    
