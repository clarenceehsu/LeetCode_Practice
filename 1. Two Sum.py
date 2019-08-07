"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

#=====================================================================================================#

# First
class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        for n in range(len(nums)):
            for m in range(len(nums) + i):
                if nums[n] + nums[m] == target: #对比值
                    return [n, m]
                i += 1

# 40ms
# 第一个尝试版本，能够成功通过，但是指针会溢出
# 多了一个i这个没有什么用的变量，在时间上会有影响，而且时间复杂度也会高，相当于自己写了一个遍历算法

#=====================================================================================================#

# Second
class Solution:
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for a in range(n + 1, len(nums)):
                if nums[a] == target - nums[n] and a != n:
                    return [n,a]

# 4876ms
# 第二个版本，成熟版本，直接非常粗暴地将两者进行对比，也是自己写了一个遍历算法，不过代码相对精简一些，而且没有错误

#=====================================================================================================#

# Third
class Solution:
    def twoSum(self, nums, target):
        l = []
        s = set()
        for i in range(len(nums)):
            if ((target - nums[i]) in s):
                l.append(nums.index(target - nums[i]))
                l.append(i)
            s.add(nums[i]) # 这个地方在构建字典
        
        return l

# 36ms
# 构建了一个非重复字典set()

#=====================================================================================================#

# Fourth
class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash: return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i # 构建字典

# 36ms
# 也是构建了一个字典，因为字典是根据哈希值来进行搜索的，所以速度会比数组的快很多