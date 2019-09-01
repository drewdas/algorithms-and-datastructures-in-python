# Write a function to see if a binary tree is "superbalanced".
# A tree is "superbalanced" if the difference between the depths 
# of any two leaf nodes is no greater than one.

# Tree 1
#       5
#      / \
#     4   2
#    / \   \
#   1   8   9


# Brainstorm
# Depth First Search
# Add to Stack as we traverse the tree


import unittest

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        self.left = BinaryTree(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTree(value)
        return self.right

def is_balanced(root):
    if root is None:
       return True
    
    depths = []

    node_stack = []
    node_stack.append((root, 0))

    while node_stack:
        node, depth = node_stack.pop()

        # check if leaf node
        if (not node.left) and (not node.right):

            # we check if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # if more than two depths or if difference between two depths greater than 1
                if ((len(depths) > 2) or (len(depths) == 2 and abs(depths[0]-depths[1])>1)):
                    return False
        else:
            if node.left:
                node_stack.append((node.left, depth+1))
            if node.right:
                node_stack.append((node.right, depth+1))
    
    return True

                 




class TestCase(unittest.TestCase):
    
    def test_full_tree(self):
        root = BinaryTree(5)
        root.insert_left(4)
        root.insert_right(2)
        root.left.insert_left(1)
        root.left.insert_right(8)
        root.right.insert_right(9)
        result = is_balanced(root)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        root = BinaryTree(6)
        left = root.insert_left(1)
        right = root.insert_right(0)
        right.insert_right(7)
        result = is_balanced(root)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        root = BinaryTree(6)
        left = root.insert_left(1)
        right = root.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(root)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = BinaryTree(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = BinaryTree(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = BinaryTree(1)
        result = is_balanced(tree)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)