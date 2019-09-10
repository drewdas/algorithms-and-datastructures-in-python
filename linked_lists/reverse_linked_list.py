# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # in a single walk through list,
        # start previous node as none
        # copy next pointer of current node to next_node
        # set next pointer of current node to previous node
        # then set previous node as current node
        # set current node to next node, to step forward
        # 1->2->3->None
        # 3->2->1->None
        current_node = head
        # prev node pointer
        previous_node = None
        # next node pointer
        next_node = None
        while current_node:
            # set 
            next_node = current_node.next
            current_node.next = previous_node
            
            # step forward
            previous_node = current_node
            current_node = next_node
        # We return previous_node because when we exit the list, 
        # current_node is None. Which means that the last node we 
        # visited previous_node was the tail of the original list, 
        # and thus the head of our reversed list. 
        return previous_node
