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

def traverse_inorder_iterative(tree_root):
    if tree_root is None:
       return None
    
    result = []
    stack = []
    current = tree_root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.value)
            current = current.right
        else:
            break
    return result


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

def traverse_preorder_iterative(node):
    result = []
    node_stack = [] 
    node_stack.append(node) 
  
    #  Pop all items one by one. Do following for every popped item 
    #   a) print it 
    #   b) push its right child 
    #   c) push its left child 
    # Note that right child is pushed first so that left 
    # is processed first */ 
    while node_stack: 
          
        # Pop the top item from stack and append it
        current_node = node_stack.pop()
        result.append(current_node.value)
          
        # Push right and left children of the popped node 
        # to stack 
        if current_node.right is not None: 
            node_stack.append(current_node.right) 
        if current_node.left is not None: 
            node_stack.append(current_node.left) 
    return result


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

    def test_inorder_iterative(self):
        node = create_tree()
        result = traverse_inorder_iterative(node)
        expected = [12, 15, 19, 20, 21, 22, 27, 32]
        self.assertEqual(result, expected)
    
    def test_preorder(self):
        node = create_tree()
        result = []
        traverse_preorder(node, result)
        expected = [20, 15, 12, 19, 22, 21, 27, 32]
        self.assertEqual(result, expected)

    def test_preorder_iterative(self):
        node = create_tree()
        result = traverse_preorder_iterative(node)
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


         