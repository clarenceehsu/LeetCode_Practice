'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

#=====================================================================================================#

# First


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        self.dfs(nums, index + 1, path + [nums[index]], res)
        self.dfs(nums, index + 1, path, res)

# 28 ms, 14 MB
# 传统的 DFS 算法。

#=====================================================================================================#