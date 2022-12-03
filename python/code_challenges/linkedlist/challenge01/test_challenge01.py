import pytest
from challenge01 import *


def test_toArray():
    linkedList = Linkedlist()
    linkedList.append(4)
    linkedList.append(5)
    linkedList.append(1)
    linkedList.append(9)

    actual = linkedList.toArray()
    expected = [4,5,1,9]
    assert actual == expected

def test_delete():
    linkedList = Linkedlist()
    linkedList.append(4)
    linkedList.append(5)
    linkedList.append(1)
    linkedList.append(9)

    wantedNode = linkedList.getNode(1)
    linkedList.removeByNode(wantedNode)
    

    actual = linkedList.toArray()
    expected = [4,5,9]
    assert actual == expected