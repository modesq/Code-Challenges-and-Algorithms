# Write your test here
import pytest
from challenge01 import buildTree


def test_buildTree():
    actual = buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).value
    expected = 3
    assert actual == expected


def test_buildTree2():
    actual = buildTree(preorder=[-1], inorder=[-1]).value
    expected = -1
    assert actual == expected
