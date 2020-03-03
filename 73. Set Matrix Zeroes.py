'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

#=====================================================================================================#

# First


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        index = []
        zero = 0
        for n in range(len(matrix)):
            for m in range(len(matrix[0])):
                if matrix[n][m] == 0:
                    index.append(m)
                    zero = 1
            if zero:
                matrix[n] = [0] * len(matrix[0])
                zero = 0
        for n in matrix:
            for m in set(index):
                n[m] = 0

# 124 ms, 13.3 MB
# 这个算法就很直观，因为需要直接修改矩阵，所以减少修改矩阵次数就可以提高一定的速度

#=====================================================================================================#