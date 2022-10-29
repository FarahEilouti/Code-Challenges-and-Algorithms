# Write your test here
import pytest
from challenge03 import LinkedList

def test_delete_tail():
    
    linkedList1 = LinkedList()

    linkedList1.append('a')
    linkedList1.append('b')
    linkedList1.append('c')
    linkedList1.append('d')
    linkedList1.append('e')

    linkedList1.delete_nth(1)

    actual = linkedList1.print()
    expected = ['a', 'b', 'c', 'd']
    assert actual == expected


def test_delete_third_from_end():
    
    linkedList1 = LinkedList()

    linkedList1.append('a')
    linkedList1.append('b')
    linkedList1.append('c')
    linkedList1.append('d')
    linkedList1.append('e')

    linkedList1.delete_nth(3)

    actual = linkedList1.print()
    expected = ['a', 'b', 'd', 'e']
    assert actual == expected

