"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

#=====================================================================================================#

# First
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        start = 0
        dt = {}
        for i,c in enumerate(s):
            if c in dt:
                start = max(start,dt[c]+1)
            maxlen = max(maxlen,i-start+1)
            dt[c] = i
        return maxlen

# 84ms
# 就是遍历数组

#=====================================================================================================#