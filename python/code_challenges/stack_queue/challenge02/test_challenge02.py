import pytest

from challenge02 import Stack

def test_is_valid(stack):
    actual=stack.is_valid("()")
    expected=True
    assert actual== expected

def test_is_valid_02(stack):
    actual=stack.is_valid("()[]{}")
    expected=True
    assert actual== expected

def test_is_valid_03(stack):
    actual=stack.is_valid("[({}]")
    expected=False
    assert actual== expected

def test_is_valid_04(stack):
    actual=stack.is_valid("[(hello)()]")
    expected=True
    assert actual== expected

def test_is_valid_05(stack):
    actual=stack.is_valid("[{(())}]")
    expected=True
    assert actual== expected

@pytest.fixture
def stack():
    stack = Stack()
    return stack