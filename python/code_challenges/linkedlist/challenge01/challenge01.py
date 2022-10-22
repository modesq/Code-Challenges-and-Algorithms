# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def add_to_tail(self, value):
        current = self.head
        node = Node(value)
        if current is None:
            head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        return head

    def add_to_head(self, addedValue):
        NewNode = Node(addedValue)
        NewNode.next = self.head
        self.head = NewNode

    def delete_node(self, deletedValue):
        current = self.head
        if current.value == deletedValue:
            self.head = current.next
        else:
            while current.next is not None:
                if current.next.value == deletedValue:
                    current.next = current.next.next
                else:
                    current = current.next

    def print_SLL(self):
        printval = self.head
        while printval:
            print(printval.data),
            printval = printval.next


sll = SLL()
sll.add_to_tail(4)
sll.add_to_tail(5)
sll.add_to_tail(1)
sll.add_to_tail(9)
sll.delete_node(5)
sll.print_SLL()
