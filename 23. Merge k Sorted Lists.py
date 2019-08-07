"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

#=====================================================================================================#

# First
class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        from heapq import heappush, heappop, heapreplace, heapify
        heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
        heapify(heap) # 将list类型转化为heap类型
        dummy = ListNode(0) # 创建链表
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next: # exhausted one linked-list
                heappop(heap) # 排序，把最小的值pop出来
            else:
                heapreplace(heap, (node.next.val, i, node.next)) # recycling tie-breaker i guarantees uniqueness
            curr.next = node    
            curr = curr.next
        return dummy.next

# 68ms
# 一道列表排序题，利用heapq（堆）函数里面的内容去完成排序。

#=====================================================================================================#

"""
Note:

heapq模块使用堆实现优先级队列。堆是一个有序的项目列表，在其中会强制执行堆叠条件。
具体讲，从n=0.heap[0]开始所有的n,heap[n]<=heap[2*n+1]和heap[n]<=heap[2*n+2],始终包含最小项。
heapq.heapify()将列表原地转换为堆。
和sort(),区别在于heap采用的是堆排序算法，sort采用的是归并排序算法。
heapq从小到大排列，sort更自由一些。
"""