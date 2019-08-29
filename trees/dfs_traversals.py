# Tree traversals through DFS using recursion

# tree
#           20
#          /  \
#        15     22
#       / \    /  \
#     12  19  21   27
#                   \
#                   32

import unittest

# Inorder traversal
# Left -> Root -> Right
# [12, 15, 19, 20, 21, 22, 27, 32]
def traverse_inorder(node, arr):
    if node:
        if node.left:
            traverse_inorder(node.left, arr)
        arr.append(node.value)
        if node.right:
            traverse_inorder(node.right, arr)
    return arr


# Preorder Traversal
# Root -> Left -> Right
# [20, 15, 12, 19, 22, 21, 27, 32]
def traverse_preorder(node, arr):
    if node:
        arr.append(node.value)
        if node.left:
            traverse_preorder(node.left, arr)
        if node.right:
            traverse_preorder(node.right, arr)
    return arr

# Postorder Traversal
# Left -> Right -> Root 
# [12, 19, 15, 32, 21, 27, 22]
def traverse_postorder(node, arr):
    if node:
        if node.left:
            traverse_preorder(node.left, arr)
        if node.right:
            traverse_preorder(node.right, arr)
        arr.append(node.value)
    return arr

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        self.left = BinaryTree(value)
    
    def insert_right(self, value):
        self.right = BinaryTree(value)


def create_tree():
    root = BinaryTree(20)
    root.insert_left(15)
    root.insert_right(22)
    root.left.insert_left(12)
    root.left.insert_right(19)
    root.right.insert_left(21)
    root.right.insert_right(27)
    root.right.right.insert_right(32)
    return root




class TestCase(unittest.TestCase):

    def test_inorder(self):
        node = create_tree()
        result = []
        traverse_inorder(node, result)
        expected = [12, 15, 19, 20, 21, 22, 27, 32]
        self.assertEqual(result, expected)
    
    def test_preorder(self):
        node = create_tree()
        result = []
        traverse_preorder(node, result)
        expected = [20, 15, 12, 19, 22, 21, 27, 32]
        self.assertEqual(result, expected)
    
    def test_postorder(self):
        node = create_tree()
        result = []
        traverse_postorder(node, result)
        expected = [15, 12, 19, 22, 21, 27, 32, 20]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


         