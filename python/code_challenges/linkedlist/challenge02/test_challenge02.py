# Write your test here
import pytest
from challenge02 import *

def test_middle_node1():
    lista =Linkedlist()

    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)

    actual = lista.Get_middle_node().value
    expected = 3
    assert actual == expected

def test_middle_node2():
    lista =Linkedlist()

    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)

    actual = lista.Get_middle_node().next.value
    expected = 4
    assert actual == expected