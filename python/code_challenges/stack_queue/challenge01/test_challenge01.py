# Write your test here
import pytest
from challenge01 import MyQueue


def test_1():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    actual =  queue.peek()
    expected = 1
    assert actual == expected


def test_2():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    actual =  queue.pop()
    expected = 1
    assert actual == expected

def test_3():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    actual =  queue.empty()
    expected = False
    assert actual == expected