'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

#=====================================================================================================#

# First


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = lastIdx = nextIdx = 0
        n = len(nums)
        while nextIdx < n - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx, max(i + nums[i] for i in range(lastIdx, nextIdx + 1))
        return ans

# 112ms, 15.9MB
# 很直接的算法，复杂度O(n)。在不同的范围内选取最大的数值进行jump即可。

#=====================================================================================================#

# Second


class Solution:
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

# 108ms, 15.9MB
# 算法与上面相同。

#=====================================================================================================#