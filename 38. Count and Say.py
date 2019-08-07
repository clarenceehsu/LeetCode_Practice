'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''

#=====================================================================================================#

# First
class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(
                r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
# 44ms, 13.2MB
# 这道题老实说题目并不是非常懂，看了别人的也是说有歧义，所以就先放着吧
# 日后有时间再来回顾一下

#=====================================================================================================#