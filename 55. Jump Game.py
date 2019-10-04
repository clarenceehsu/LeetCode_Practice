'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

#=====================================================================================================#

# First


class Solution:
    def canJump(self, n: List[int]) -> bool:
    	m = 0
    	for i in range(len(n)-1):
    		m = max(m, n[i] + i)
    		if n[i] != 0: continue
    		if m <= i: return False
    	return True

# 104ms, 16.1MB
# Jumpgame 的解法，遍历每一个元素是否能够。m <= i 判断了中间的元素是否能够到下一个元素，到不了就失败返回 FALSE。

#=====================================================================================================#