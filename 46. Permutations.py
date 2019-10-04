'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

#=====================================================================================================#

# First


class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# 40ms, 13.8MB
# 经典的 DFS 算法。

#=====================================================================================================#