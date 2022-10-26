# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        checks if the SLL is empty
        """
        return self.head == None

    # def append(self, node):
    #     if self.head is None:
    #         self.head = node
    #     else:
    #         current = self.head
    #     while current.next is not None:
    #         current = current.next
    #     current.next = node

    def addToTail(self, value):
        current = self.head
        node = Node(value)
        if current is None:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        return self.head

    def addToHead(self, value, *args):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return new_node

    # challenge two
    def deleteNode(self, key):
        """
        this method takes a key and checks where it exists inside the SLL, if it does it returns the __str__ fucntion but
        if it doesnt exist in the SLL it returns "the SLL is empty"
        """
        current = self.head
        if self.isEmpty():
            return "the SLL is empty"
        if current is not None:
            if current.value == key:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.value == key:
                break
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None
        return self.__str__()

    # challenge three
    def deleteNthFromTail(self, n):
        """
        this method deletes the nth node from the tail of the SLL
        """
        first = self.head
        second = self.head
        for i in range(n):
            if second.next == None:
                if i == n - 1:
                    self.head = self.head.next
                return self.head
            second = second.next
        while second.next != None:
            second = second.next
            first = first.next
        first.next = first.next.next
        return self.head

    def findMiddle(self):
        """
        this method is quite simple, it moves both pointers(current and middle_node), current moving twice as fast as
        middle_node, when current reaches the end of the SLL, middle_node reaches its middle_node because its moving half
        as fast as current
        """
        current = self.head
        middle_node = self.head
        while current.next is not None:
            current = current.next.next
            middle_node = middle_node.next
        return middle_node.value

    def search(self, key):
        current = self.head
        while self.isEmpty():
            if current.value == key:
                return True
            current = current.next
        return False

    def displaySLL(self):
        current = self.head
        if self.isEmpty():
            print("empty")
        while current is not None:
            print(current.value),
            current = current.next

    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
        while current:
            output += f"{current.value}-->"
            current = current.next
        output += "None"
        return output


def constructSLL(values):
    temp = SLL()
    current = Node(None)

    for value in values:
        current = temp.addToTail(value)
        current = current.next
    return temp


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    sll = constructSLL(values)
    sll.displaySLL()
    print("")
    # sll.deleteNode(3)
    sll.displaySLL()
    print(" ")
    sll.deleteNthFromTail(2)
    sll.displaySLL()
