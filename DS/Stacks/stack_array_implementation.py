class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def push(self, value):
        self.stack.append(value)
        self.length += 1
        return self.stack

    def pop(self):
        self.stack.pop()
        self.length -= 1
        return self.stack

    def peek(self):
        if self.length == 0:
            return None
        return self.stack[self.length-1]

    def is_empty(self):
        if self.length == 0:
            return "Empty"
        return "Bc lag toh rha hai kuch toh hai."


my_stack = Stack()
my_stack.push("google")
my_stack.push("udemy")
my_stack.push("youtube")
print(my_stack.stack)
my_stack.pop()
print(my_stack.stack)
print(my_stack.peek())
print(my_stack.is_empty())
