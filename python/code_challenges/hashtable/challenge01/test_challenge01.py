# Write your test here
# Write your test here
import pytest
from challenge01 import *


def test_sum_bst():
    tree1 = Tree(7)
    tree1.left = Tree(2)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(5)
    tree1.right = Tree(9)
    tree1.right.right = Tree(14)
    actual = findTarget(tree1, 3)
    expected = True
    assert actual == expected


def test_sum_bst_tow():
    tree1 = Tree(7)
    tree1.left = Tree(2)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(5)
    tree1.right = Tree(9)
    tree1.right.right = Tree(14)
    actual = findTarget(tree1, 4)
    expected = False
    assert actual == expected
