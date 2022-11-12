# Write your test here
import pytest
from challenge03 import sortedArrayToBST

def test_buildTree1():
    nums = [-10,-3,0,5,9]
    actual = sortedArrayToBST(nums).value
    expected = 0
    assert actual == expected

def test_buildTree2():
    nums = [1,3]
    actual = sortedArrayToBST(nums).value
    expected = 3
    assert actual == expected

def test_buildTree3():
    nums = [1,6, 9, 12, 15, 16, 17]
    actual = sortedArrayToBST(nums).value
    expected = 12
    assert actual == expected
    
def test_buildTree4():
    nums = []
    actual = sortedArrayToBST(nums)
    expected = None
    assert actual == expected
