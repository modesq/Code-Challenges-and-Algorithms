# Write your test here
import pytest
from challenge03 import SLL

def test_deleteNthFromTail():
    actual = sll_example.deleteNthFromTail(2)
    expected = 1
    assert expected == actual

@pytest.fixture
def sll_example():
    sll = SLL()
    sll.addToTail(1)
    sll.addToTail(2)
    sll.addToTail(3)
    sll.addToTail(4)
    sll.addToTail(5)
    return sll