class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ArrayToBST(nums):

    """
    This Functions Recives Sorted Array,
    and it Converts it to A Height Balanced Search Tree
    """

    if not nums:
        return None

    # getting the mid
    mid = len(nums) // 2
    node = Node(nums[mid])

    node.left = ArrayToBST(nums[:mid])
    node.right = ArrayToBST(nums[mid + 1 :])
    return node


def bfs(root):

    """
    Breadth First Search (BFS), It take tree as input
    and it returns the value of each node in every level for left to right
    """

    if root is None:
        return
    queue = [root]
    array = []
    while len(queue) > 0:
        cur_node = queue.pop(0)
        array.append(cur_node.val)
        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.left is None and len(queue) > 0:
            array.append(None)

        if cur_node.right is not None:
            queue.append(cur_node.right)

    return array
