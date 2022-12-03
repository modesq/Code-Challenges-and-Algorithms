# Write your test here
import pytest
from challenge01 import *





def test_inOrder():
    tree = Tree()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    head = tree.buildTree(preorder,inorder)

    actual = tree.toArray_inorder(head)
    expected = inorder

    assert actual == expected


def test_preOrder():
    tree = Tree()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    head = tree.buildTree(preorder,inorder)

    actual = tree.toArray_Preorder(head)
    expected = preorder

    assert actual == expected