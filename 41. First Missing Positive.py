'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

#=====================================================================================================#

# First

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

# 44ms, 13.6MB
# 先进行了O(n)的简单排序，然后再遍历一遍判断哪个值不等于指针的值 + 1。因为要求是 O(n)，所以没有办法只能够这么算。

#=====================================================================================================#

# Second

class Solution(object):
    def firstMissingPositive(self, nums):

        nums.sort()
        n = 1
        for num in nums:
            if num == n:
                n += 1
        return n

# 44ms, 13.7MB
# 这个是我最初直接想出来的算法，就是排序之后找出空缺就行了。但是复杂度 O(nlogn)，所以不能算做正解。

#=====================================================================================================#