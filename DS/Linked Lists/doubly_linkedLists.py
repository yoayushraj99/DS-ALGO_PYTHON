class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        self.head = {'prev': None, 'value': value, 'next': None}
        self.tail = self.head
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = {'prev': self.tail, 'value': value, 'next': None}
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self.tail

    def prepend(self, value):
        new_node = {'prev': None, 'value': value, 'next': self.head}
        self.head = new_node
        self.length += 1
        return self.head

    def traverse_to_node(self, index):
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node['next']
        return current_node

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        else:
            new_node = {'prev': self.traverse_to_node(index), 'value': value, 'next': self.traverse_to_node(index)['next']}
            self.traverse_to_node(index)['next'] = new_node
            self.length += 1
            return self.head

    def remove(self, index, value):
        if index == 0:
            self.head = self.head['next']
            return self.head
        else:
            current_node = self.traverse_to_node(index)
            current_node['next'] = current_node['next']['next']
            self.length -= 1
            return self.head


linked_list = DoublyLinkedList(2)
print(linked_list.append(3))
print(linked_list)
