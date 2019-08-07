"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

#=====================================================================================================#

# First
class Solution:
    def isMatch(self, s, p):
        memo = {}
        def dp(si, pi):
            if pi >= len(p): return si == len(s)
            if si >= len(s): return pi + 1 < len(p) and p[pi + 1] == '*' and dp(si, pi + 2)
            if (si, pi) not in memo:
                matched = p[pi] == '.' or p[pi] == s[si]
                if pi + 1 < len(p) and p[pi + 1] == '*':
                    memo[(si, pi)] = dp(si, pi + 2) or (matched and dp(si + 1, pi))
                else:
                    memo[(si, pi)] = matched and dp(si + 1, pi + 1)
            return memo[(si, pi)]
        return dp(0, 0)

# 52ms
# 用了递归

#=====================================================================================================#