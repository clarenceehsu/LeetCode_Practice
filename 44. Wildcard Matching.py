'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

#=====================================================================================================#

# First


class Solution:
    def isMatch(self, s, p):
        sn, pn = len(s), len(p)
        si = pi = 0
        save_si, save_pi = None, None
        while si < sn:
            if pi < pn and (p[pi] == '?' or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < pn and p[pi] == '*':
                # Meet "*", save si and pi, searching for next character
                save_si, save_pi = si + 1, pi
                pi += 1
            elif save_pi is not None:
                # Dead end, restore si and pi, carry on.
                si, pi = save_si, save_pi
            else:
                return False
        # Check trailing "*"
        return p[pi:].count("*") == pn - pi

# 48ms, 14MB
# 首先设置初始值，减小后续的计算调用；然后进行两个字符串的匹配，匹配到*的时候p加一，再匹配到p再加1，如果匹配到字母且与原来匹配的不符，p减一回到*，然后s+1
# 其实就是O(n^2)的匹配了。

#=====================================================================================================#