# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    current_node = head
    length = 1
    while current_node.next:
        current_node = current_node.next
        length += 1
    
    if length == 1:
        return None
    
    how_far_to_go = length - n
    current_node = head
    for i in range(how_far_to_go):
        prev = current_node
        current_node = current_node.next
    
    if current_node.next:
        current_node.val = current_node.next.val
        current_node.next = current_node.next.next
    else:
        prev.next = None
    
    return head