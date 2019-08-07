"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

#=====================================================================================================#

# First
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res

# 812ms
# 先把数组给排序，然后从左端开始i循环，并新建两个指针，从左右到中间，计算三个数的和，并且也不能忘记去重

#=====================================================================================================#

# Second
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l +=1 
                elif s > 0: r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1; r -= 1
        return res

# 776ms
# 原理与上面一样

#=====================================================================================================#