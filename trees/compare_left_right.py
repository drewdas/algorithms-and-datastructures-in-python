


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
    
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
    
def traverse(node, arr=[]):
    current_node = node
    if current_node:
        if current_node.left:
            traverse(current_node.left, arr)
        arr.append(current_node.value)
        if current_node.right:
            traverse(current_node.right, arr)
    return arr

def sum_arr(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] != -1:
            sum += arr[i]
    return sum

def insert_level_order(arr, root, i, n):
    if i < n:
        temp = BinaryTreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2*i+1, n)
        root.right = insert_level_order(arr, root.right, 2*i+2, n)
    return root

def solution(arr):
    if arr == []:
        return ""
    n = len(arr)
    if n == 1:
        return ""
    root = [None]
    root = insert_level_order(arr, root, 0, n)
    
    left_arr = []
    right_arr = []
    traverse(root.left, left_arr)
    traverse(root.right, right_arr)
    
    if sum_arr(left_arr) > sum_arr(right_arr):
        return "Left"
    
    if sum_arr(left_arr) < sum_arr(right_arr):
        return "Right"
    
    
    return ""
    
        
