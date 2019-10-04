"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

#=====================================================================================================#

# First
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        pre, cur = head, head
        for i in range(n): cur = cur.next
        if not cur: return head.next
        while cur.next:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return head

# 40ms, 6.4MB
# 

#=====================================================================================================#