class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    # Go left
                    if not current_node.left:
                        current_node.left = new_node
                        return
                    current_node = current_node.left
                else:
                    # Go right
                    if not current_node.right:
                        current_node.right = new_node
                        return
                    current_node = current_node.right

    def lookup(self, value):
        if self.root is None:
            return None
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return value
            elif value < current_node.value:
                # Go left
                current_node = current_node.left
            elif value > current_node.value:
                # Go right
                current_node = current_node.right
