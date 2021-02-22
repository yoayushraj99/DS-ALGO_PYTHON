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
        return self.top.value

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
            pop_value = self.top.value
            self.top = self.top.next
            self.length -= 1
            return pop_value

    def is_empty(self):
        if self.top is None:
            return True
        return False


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('youtube')
print(my_stack.peek())
# youtube

print(my_stack.pop())
# youtube

print(my_stack.peek())
# udemy

print(my_stack.is_empty())
# False




