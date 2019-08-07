"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

#=====================================================================================================#

# First
class Solution:
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a

# 40ms, 6.5MB
# 列表的比较，然后直接用递归继续即可

#=====================================================================================================#