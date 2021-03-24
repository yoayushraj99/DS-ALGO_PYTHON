from binary_search_tree import BinarySearchTree as Bst

tree = Bst()
tree.insert(9)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(20)
tree.insert(15)
tree.insert(170)


def dfs_inorder(node, array):
    if node.left:
        dfs_inorder(node.left, array)
    array.append(node.value)
    if node.right:
        dfs_inorder(node.right, array)
    return array


def dfs_preorder(node, array):
    array.append(node.value)
    if node.left:
        dfs_preorder(node.left, array)
    if node.right:
        dfs_preorder(node.right, array)
    return array


def dfs_postorder(node, array):
    if node.left:
        dfs_postorder(node.left, array)
    if node.right:
        dfs_postorder(node.right, array)
    array.append(node.value)
    return array


#        9
#   4         20
# 1   6    15    170

print(dfs_inorder(tree.root, []))
# [1, 4, 6, 9, 15, 20, 170]

print(dfs_preorder(tree.root, []))
# [9, 4, 1, 6, 20, 15, 170]

print(dfs_postorder(tree.root, []))
# [1, 6, 4, 15, 170, 20, 9]
