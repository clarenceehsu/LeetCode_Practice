"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

#=====================================================================================================#

# First
class Solution:
    def strStr(self, haystack, needle):
        a = len(needle)
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(a):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1

# 36ms, 12.6MB
# 很简单的匹配，needle一旦不符合就会break，然后从下一个开始，如果needle匹配完了就返回i。

#=====================================================================================================#

# Second
class Solution:
    def getRight(self,str):
        n = len(str)
        if n <= 0:
            return []
        right = [ -1 for i in range(256)]
        for i,c in enumerate(str):
            right[ord(c)] =  i
        return right
    def strStr(self, haystack, needle):
        right = self.getRight(needle)
        nn = len(needle)
        nh = len(haystack)
        i = 0
        while i <= nh-nn:
            j = nn - 1
            while j >= 0:
                if haystack[i+j] != needle[j]:
                    if i+nn < nh:
                        skip = nn - right[ord(haystack[i+nn])]
                    else:
                        return -1
                    break
                j -= 1
            if j == -1:
                return i
            i += skip
        return -1

# 36ms, 12.5MB
# 上面算法的复杂版，速度大体相似。

#=====================================================================================================#