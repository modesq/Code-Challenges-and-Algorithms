import pytest
from challenge01 import Queue


def test_push(q):
    q.push(12)
    actual = q.peek()
    expected = 1
    assert actual == expected


def test_pop(q):
    actual = q.pop()
    expected = 1
    assert actual == expected


def test_empty_peek():
    empty = Queue()
    actual = empty.peek()
    expected = "This Queue is empty"
    assert actual == expected


def test_peek(q):
    actual = q.peek()
    expected = 1
    assert actual == expected


def test_is_empty(q):
    actual = q.is_empty()
    expected = False
    assert actual == expected


@pytest.fixture
def q():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    return q