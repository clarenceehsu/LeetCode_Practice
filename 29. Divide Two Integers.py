"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""

#=====================================================================================================#

# First
class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        positive = (dividend < 0) is (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        ans = a // b
        if not positive:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)

# 52ms, 12.5MB
# 因为直接用//去运算的话，一正一负运算会有问题；
# 所以先把符号用positive来表示，然后再取绝对值作除法，最后套上符号输出。

#=====================================================================================================#

# Second
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

# 48ms, 12.5MB
# 其他的大致与上面的相似，不同的是这个算法里面运用了二进制的移位算法；
# 所以会快上一些，但是差别不大。

#=====================================================================================================#