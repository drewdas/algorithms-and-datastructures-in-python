# Write a function to see if a binary tree ↴ is "superbalanced".
# A tree is "superbalanced" if the difference between the depths 
# of any two leaf nodes is no greater than one.
import unittest

def is_balanced(tree):
    pass

class TestCase(unittest.TestCase):

    class BinaryTree:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        
        def insert_left(self, value):
            self.left = BinaryTree(value)
        
        def insert_right(self, value):
            self.right = BinaryTree(value)
    
    def test_case_1(self):

