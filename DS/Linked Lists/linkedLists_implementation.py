# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedLists:
    def __init__(self, value):
        self.head = {'value': value, 'next': None}
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = {'value': value, 'next': None}
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self.tail

    def prepend(self, value):
        new_node = {'value': value, 'next': self.head}
        self.head = new_node
        self.length += 1
        return self.head, self.length
    
    def traverse_to_node(self, index):
        current_node = self.head
        for i in range(0, index - 1):
            current_node = current_node['next']
        return current_node
    
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        else:
            new_node = {'value': value, 'next': None}
            current_node = self.traverse_to_node(index)
            new_node['next'] = current_node['next']
            current_node['next'] = new_node
            self.length += 1
            return self.head, self.length

    def remove(self, index, value):
        if index == 0:
            self.head = self.head['next']
            return self.head
        else:
            current_node = self.traverse_to_node(index)
            new_node = current_node['next']['next']
            current_node['next'] = new_node
            return self.head


myLinkedLists = LinkedLists(10)
# print(myLinkedLists)
print(myLinkedLists.append(10))
print(myLinkedLists.append(8))
print(myLinkedLists.prepend(5))
print(myLinkedLists.insert(2, 4))
print(myLinkedLists.remove(2, 4))
