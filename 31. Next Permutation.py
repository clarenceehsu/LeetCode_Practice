"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

#=====================================================================================================#

# First
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]: i -= 1
        if i > 0:
            j, pre = len(nums) - 1, nums[i - 1]
            while j >= i and nums[j] <= pre: j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        k = len(nums) - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i, k = i + 1, k - 1

# 48ms, 13.2MB
# 这个算法比较简单，首先是从数组后面去遍历找到比i + 1低的数i
# 从后面再一次遍历寻找比i大的数a并且交换位置
# 把a后面的数逆序排列

#=====================================================================================================#

# Second
class Solution(object):
    def nextPermutation(self, nums):

        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i-1] < nums[i]: # first one violates the trend
              j = i-1
              break
            i-=1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: # 
                nums[i], nums[j] = nums[j], nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return

# 48ms, 13.2MB
# 基本上同上面一样

#=====================================================================================================#