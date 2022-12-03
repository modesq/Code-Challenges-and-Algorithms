import pytest
from challenge03 import *


def test1():
    lista = Linkedlist()

    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)

    actual = lista.Remove_nTh_node(2)
    expected = [1, 2, 3, 5]
    assert actual == expected


def test2():
    lista = Linkedlist()

    lista.append(1)
    lista.append(2)

    actual = lista.Remove_nTh_node(2)
    expected = [2]
    assert actual == expected
