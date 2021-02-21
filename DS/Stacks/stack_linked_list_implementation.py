class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.top is None:
            return None

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None

    def is_empty(self):
        if self.top is None:
            return "Empty"
        return "hmm lag toh rha hai kuch toh hai."


my_stack = Stack()
my_stack.push('google')
print(my_stack.top.value)
