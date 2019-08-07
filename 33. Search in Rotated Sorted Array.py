"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

#=====================================================================================================#

# First
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# 40ms, 13.3MB
# 原理很简单，就是nums数组本来就是以中间为分界，左右都是升序排列
# 直接以中间为界即可

#=====================================================================================================#

# Second
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums)-1)
        
    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = (start+end)/2
        if nums[mid] == target:
            return mid
        if nums[start] <= target < nums[mid]: # left side is sorted and has target
            return self.binarySearch(nums, target, start, mid-1)
        elif nums[mid] < target <= nums[end]: # right side is sorted and has target
            return self.binarySearch(nums, target, mid+1, end)
        elif nums[mid] > nums[end]: # right side is pivoted
            return self.binarySearch(nums, target, mid+1, end)
        else: # left side is pivoted
            return self.binarySearch(nums, target, start, mid-1)

# 40ms, 13.6MB
# 算法与上面一样

#=====================================================================================================#