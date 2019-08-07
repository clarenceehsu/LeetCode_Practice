"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

#=====================================================================================================#

# First
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        if n%2:
            return(nums3[int(n/2)])
        return((nums3[int(n/2) - 1] + nums3[int(n / 2)])/2)
# 96ms
# 将两个数组组合在一起然后排序，然后求出中位数

#=====================================================================================================#