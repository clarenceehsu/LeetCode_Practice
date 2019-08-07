"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

#=====================================================================================================#

# First
class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))

# 40ms, 6.8MB
# 回溯解法，即直接将所有符合条件的穷举出来，递归的时候的函数不影响主函数

#=====================================================================================================#