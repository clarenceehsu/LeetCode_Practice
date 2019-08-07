"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

#=====================================================================================================#

#First
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0 # 进位buff
        head = node = ListNode('#') #定义一个链表
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 #如果空就是0
            carry, rem = divmod(carry + val1 + val2, 10) #divmod得出一个商余数组[(a // b, a % b)]
            node.next = ListNode(rem)
            node = node.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None # 这两步将l1，l2的值更新，并能够确保最后一位在none
        if carry:
            node.next = ListNode(carry) # 最后一位如果还是carry那就链接到carry
        return head.next # head代替node来输出

# 100ms
# 这里主要运用到了链表的一些知识

#=====================================================================================================#

#Second
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

# 96ms
# 直白得一批，很简单又快捷，比上面的更好理解而且还快

#=====================================================================================================#