"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

#=====================================================================================================#

# First
class Solution(object):
    def longestValidParentheses(self, s):
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (()) 
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid 
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now

# 56ms, 13.2MB
# 这种算法就是举出不同的情况然后按照情况去进行计算

#=====================================================================================================#

# Second
class Solution(object):
    def longestValidParentheses(self, s):
        stack, ans = [], 0
        for i,v in enumerate(")"+s):
          if v == ")" and stack and stack[-1][1] == "(":
            stack.pop()
            ans = max(ans, i - stack[-1][0])
          else:
            stack.append((i, v))
        return ans

# 60ms, 14.9MB
# 这个是利用了堆栈，然后就pop出来

#=====================================================================================================#