"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

#=====================================================================================================#

# First
class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        return str(x) == str(x)[::-1]

# 232ms
# 先将数字转换为字符串，然后再将其倒序，然后再进行比较

#=====================================================================================================#

# Second
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        else:
            x_str = str(x)
            i = 0
            j = len(x_str)-1

            if j == 0:
                return True

            while (x_str[i] == x_str[j]) and (i <= j):
                i = i + 1
                j = j - 1

            if i < j:
                return False
            else:
                return True

# 240ms
# 这个方法就是不使用字符转换的方法，直接进行计算来到倒序

#=====================================================================================================#