'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''

#=====================================================================================================#

# First


class Solution(object):
    def getPermutation(self, n, k):
        res = ''
        nums = [i for i in range(1,n+1)]
        for i in range(n-1,0,-1):
            base = math.factorial(i)
            current = 0
            while k > base:
                k -= base
                current += 1
            res += str(nums[current])
            nums.pop(current)
        res += str(nums[0])
        return res

# 20ms, 13.9MB

#=====================================================================================================#