from binary_search_tree import BinarySearchTree as Bst

tree = Bst()
tree.insert(9)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(20)
tree.insert(15)
tree.insert(170)


# Method-1

def breadth_first_search():
    current_node = tree.root
    array = []
    queue = [current_node]
    while len(queue) > 0:
        current_node = queue.pop(0)
        array.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return array


print(breadth_first_search())


# [9, 4, 20, 1, 6, 15, 170]


# Method-2

def breadth_first_search_recursion(array, queue):
    if not len(queue):
        return array
    current_node = queue.pop(0)
    array.append(current_node.value)
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
    return breadth_first_search_recursion(array, queue)


print(breadth_first_search_recursion([], [tree.root]))
# [9, 4, 20, 1, 6, 15, 170]
