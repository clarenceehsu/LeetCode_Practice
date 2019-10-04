"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

#=====================================================================================================#

# First
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: # break early 
                    return res
        return res

# 140ms
# 跟上一道题差不多的算法

#=====================================================================================================#

# Second
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        closest = []
        
        for i, num in enumerate(nums[0:-2]):
            l,r = i+1, length-1
						
            # different with others' solution
						
            if num+nums[r]+nums[r-1] < target:
                closest.append(num+nums[r]+nums[r-1])
            elif num+nums[l]+nums[l+1] > target:
                closest.append(num+nums[l]+nums[l+1])
            else:
                while l < r:
                    closest.append(num+nums[l]+nums[r])
                    if num+nums[l]+nums[r] < target:
                        l += 1
                    elif num+nums[l]+nums[r] > target:
                        r -= 1
                    else:
                        return target
                    
        closest.sort(key=lambda x:abs(x-target))
        return closest[0]

# 40ms
# 上面算法的改进，加了两条if

#=====================================================================================================#