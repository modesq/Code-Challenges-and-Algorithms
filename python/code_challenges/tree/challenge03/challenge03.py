# Write here the code challenge solution
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


def sortedArrayToBST(nums: list[int]):
    """
    this fucntion takes a sorted list and then iterates over using recursion and the inner function "makeBSt()" until we reach the base case, then returns the root node
    """

    def makeBST(nums, start, end):
        if start >= end:
            return None
        return TreeNode(
            value=nums[(start + end) // 2],
            left=makeBST(nums, start, (start + end) // 2),
            right=makeBST(nums, 1 + ((start + end) // 2), end),
        )

    return makeBST(nums, 0, len(nums))
