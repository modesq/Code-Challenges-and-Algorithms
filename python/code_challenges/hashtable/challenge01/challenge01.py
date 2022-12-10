# Write here the code challenge solution
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return self.root

        current = self.root
        while True:
            if current.value > node.value:
                if current.left == None:
                    current.left = node
                    return self.root
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    return self.root
                current = current.right


def findTarget(node, k: int):
    """
    function that takes a Binary Search tree and an integer as a parameter. Return True if Binary search tree has two elements that their summation is the given integer.
    """
    def dfs(node, seen):
        if node == None:
            return False
        complement = k - node.value
        if complement in seen:
            return True
        seen.add(node.value)
        return dfs(node.left, seen) or dfs(node.right, seen)

    return dfs(node, set())