# Write your test here
import pytest
from challenge01 import SLL, Node


def test_deleteNode(sll):
    actual = sll.deleteNode(5)
    expected = "4-->1-->9-->None"
    assert expected == actual

def test_deleteNode2(sll):
    actual = sll.deleteNode(1)
    expected = "4-->5-->9-->None"
    assert expected == actual


@pytest.fixture
def sll():
    sll1 = SLL()
    sll1.addToTail(4)
    sll1.addToTail(5)
    sll1.addToTail(1)
    sll1.addToTail(9)
    return sll1
