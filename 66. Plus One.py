'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

#=====================================================================================================#

# First


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n<1: return []
        digits[n-1] += 1
        for one in range(len(digits)):
            if digits[n-one-1] > 9:
                digits[n-one-1] %= 10
                if n-one-2 >= 0:
                    digits[n-one-2] += 1
                else:
                    digits[0] = 0
                    digits.insert(0,1)
        return digits

# 24ms, 13.9MB
# 算法代码直观。

#=====================================================================================================#