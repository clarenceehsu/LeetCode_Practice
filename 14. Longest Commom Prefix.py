"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""

#=====================================================================================================#

# First
class Solution:
    def longestCommonPrefix(self, strs):        
            i = 0
            for x in zip(*strs):            
                if len(set(x)) > 1: return strs[0][:i]            
                i += 1            
            return strs[0][:i] if strs else ''

# 36ms
# 先将其用zip压缩然后解压，形成一个list

#=====================================================================================================#