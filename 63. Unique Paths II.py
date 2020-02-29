'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

#=====================================================================================================#

# First


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [1] + [0] * (len(obstacleGrid[0])-1)
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j] + dp[j-1] if j > 0 else dp[j]
        return dp[-1]

# 52ms, 13.8MB
# 这里主要用的是 DP （动态规划）算法，他把整个矩阵看做类似于二叉树的形式。如果有路就标 1，被挡住就标 0；
# 然后下一行里面在上面算法的同时，也会检查此行和上一行的关系，如果此行的元素上一行是 0，那么也会归 0。

#=====================================================================================================#