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

    def is_valid(self, s: str):
        """
        this method takes a string and checks if the parentheses are placed correctly and each one is closed properly
        then retruns true if it, and false otherwise
        """
        if len(s) % 2 != 0:
            return False
        parentheses = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in parentheses.keys():
                self.push(i)
            else:
                if self.is_empty():
                    return False
                a = self.pop()
                if i != parentheses[a]:
                    return False
        return True

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


if __name__ == "__main__":
    stack1 = Stack()
    print(stack1.is_valid("[({}]"))

    stack2 = Stack()
    print(stack1.is_valid("()[]{}"))