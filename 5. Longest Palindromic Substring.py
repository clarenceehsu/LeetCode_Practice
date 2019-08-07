"""

"""

#=====================================================================================================#

# First
class Solution:
    def longestPalindrome(self, s):
        lens = len(s)
        if lens <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < lens:
            if lens - i <= maxLen / 2: break
            j, k = i, i
            while k < lens - 1 and s[k] == s[k + 1]: k += 1
            i = k + 1
            while k < lens - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
            if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]

# 72ms
# 先遍历，判断满不满足条件，满足则继续进行判断左右两端满不满足

#=====================================================================================================#