import pytest
from challenge03 import *


def test_1():

    tree = ArrayToBST([-10, -3, 0, 5, 9])

    actual = bfs(tree)
    expected = [0, -3, 9, -10, None, 5]

    assert actual == expected


def test_2():

    tree = ArrayToBST([1, 3])

    actual = bfs(tree)
    expected = [3, 1]

    assert actual == expected
