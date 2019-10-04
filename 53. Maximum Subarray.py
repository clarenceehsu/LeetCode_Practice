'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

#=====================================================================================================#

# First


class Solution:
    def maxSubArray(self, N: List[int]) -> int:
    	r, l, M = len(N), 0, max(N)
    	while l < r:
    		n, i = 0, l
    		for y in range(i, r):
    			n, l = n + N[l], l + 1
    			if n < 0: break
    			if n > M: M = n
    	return M

# 68ms, 14.6MB
# 这是双指针、DP 算法

#=====================================================================================================#