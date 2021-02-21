class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.top.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.top is None:
            self.bottom = new_node
            self.top = self.bottom
        else:
            self.bottom.next = new_node
            self.bottom = new_node
        self.length += 1

    def dequeue(self):
        if self.top is None:
            return None
        else:
            self.top = self.top.next
            self.length -= 1


my_queue = Queue()
my_queue.enqueue("Ayush")
my_queue.enqueue("Angela")
my_queue.enqueue("Andrew")
print(my_queue.top.value)
# Ayush

my_queue.dequeue()
print(my_queue.top.value)
# Angela

print(my_queue.peek())
# Angela
