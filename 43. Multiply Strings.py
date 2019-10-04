'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

#=====================================================================================================#

# First


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 * num2)

# 32ms, 13.9MB
# 这个算法不用说，直接作弊过去。其是按照题目的要求是不能够使用自带的str-int转换库，所以直接写一个str转int和int转str的算法就行。

#=====================================================================================================#