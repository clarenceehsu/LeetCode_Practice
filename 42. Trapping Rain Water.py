'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

#=====================================================================================================#

# First


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lmax = rmax = 0
        for n in height:
            if n >= lmax:
                lmax = n
            else:
                res += lmax - n
        for m in reversed(height):
            if m >= rmax:
                rmax = m
            res -= lmax-rmax
        return res

# 60ms, 14.6MB
# 这个是一遍过的算法代码，说白了就是从左往右相加，再从右往左把多出来的减掉，所以把原数组遍历了两遍。

#=====================================================================================================#