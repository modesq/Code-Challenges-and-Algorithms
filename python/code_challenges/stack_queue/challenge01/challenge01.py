class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        """
        takes a value and pushes it to the top of the stack
        """
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """
        pops the top node out of the stack
        """
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return f"This {self.__class__.__name__} is empty"

    def peek(self):
        """
        returns the top value of the top node in the stack
        """
        if self.top:
            return self.top.value
        else:
            return f"This {self.__class__.__name__} is empty"

    def is_empty(self):
        """
        checks if the stack is empty and returns a boolean value based on
        that
        """
        return self.size == 0

    def get_size(self):
        """
        returns the size of the stack
        """
        return self.size


class Queue:
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()

    def push(self, x: int):
        """
        pushed the values int the queue using the stack its built upon
        """
        self.pushStack.push(x)

    def pop(self):
        """
        pops the front node in the queue
        """
        if self.is_empty():
            print("Queue is Empty")
            return
        if self.popStack.size:
            return self.pop_stpopStackack.pop()
        else:
            while self.pushStack.size:
                self.popStack.push(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self):
        """
        peeks into the front node in the queue
        """
        if self.is_empty():
            return f"This {self.__class__.__name__} is empty"
        else:
            while self.pushStack.size:
                self.popStack.push(self.pushStack.pop())
            return self.popStack.peek()

    def is_empty(self):
        """ "
        checks if the stacks that the queue is built upon are empty and
        returns a boolean value based on that
        """
        return self.pushStack.size == 0 and self.popStack.size == 0


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.push(1)
    #  queue is: [1]
    myQueue.push(2)
    #  queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek()
    #  return 1
    myQueue.pop()
    #  return 1, queue is [2]
    myQueue.empty()
    #  return false
