# Write here the code challenge solution
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


def buildTree(preorder, inorder):
    """
    this function builds a tree
    """
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind + 1 :])
        return root
