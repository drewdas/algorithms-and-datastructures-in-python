class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        self.left = BinaryTree(value)
    
    def insert_right(self, value):
        self.right = BinaryTree(value)

def bst_validator(tree_root):
    if tree_root is None:
        return True
    
    node_stack = []

    upper_bound = float("inf")
    lower_bound = -float("inf")
    node_stack.append((tree_root, lower_bound, upper_bound))
    
    while node_stack:
        current_node, lower_bound, upper_bound = node_stack.pop()

        if (current_node.value <= lower_bound) or (current_node.value >= upper_bound):
            return False

        if current_node.left:
            node_stack.append((current_node.left, lower_bound, current_node.value))
        
        if current_node.right:
            node_stack.append((current_node.right, current_node.value, upper_bound))
    
    return True
        

def full_tree():
    root = BinaryTree(5)
    root.insert_left(3)
    root.insert_right(7)
    root.left.insert_left(1)
    root.left.insert_right(9)
    root.right.insert_right(9)
    return print(bst_validator(root))

full_tree()

