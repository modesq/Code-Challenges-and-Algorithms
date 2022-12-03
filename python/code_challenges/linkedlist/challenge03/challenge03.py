class Node:
    def __init__(self, value):

        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.links = []
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.length += 1
            self.links.append(value)

        else:
            currentNode = self.head

            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = new_node
            self.links.append(value)
            self.length += 1

    def toArray(self):
        result = []
        currentNode = self.head
        while currentNode != None:
            result.append(currentNode.value)
            currentNode = currentNode.next  # None
        return result

    def remove_ByNode(self, node: Node):
        next_node = node.next
        node.value = next_node.value
        node.next = next_node.next
        next_node = None

        return self.toArray()

    def getNode_byValue(self, val):
        currentNode = self.head
        wantedNode = None
        while currentNode.value != val:
            currentNode = currentNode.next
        wantedNode = currentNode
        return wantedNode

    def Get_middle_node(self):
        current_list = self.toArray()
        middle_index = len(current_list) // 2
        middle_value = current_list[middle_index]
        return self.getNode_byValue(middle_value)

    def Remove_nTh_node(self, num):
        """
        Counting the Nodes
        Traversing to the leader Node (node before  the wanted node)
        Then updating the leader node
        If nth > count of the linked list, None will be returned
        """
        currentNode = self.head
        count = 0
        while currentNode != None:  # Counting the nodes
            count += 1
            currentNode = currentNode.next

        if num > count:
            return None

        if num == count:  # Removing the Head
            return self.remove_ByNode(self.head)
        idx = 1
        currentNode = self.head
        while count - idx != num:
            idx += 1
            currentNode = currentNode.next
        leaderNode = currentNode
        leaderNode.next = leaderNode.next.next
        return self.toArray()

