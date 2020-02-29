'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

#=====================================================================================================#

# First


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if i == 0:
                for j in range(1, n):
                    grid[i][j] += grid[i][j - 1]
                continue
            for j in range(n):
                if j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] = min(grid[i][j] + grid[i][j - 1], grid[i][j] + grid[i - 1][j])

        return grid[-1][-1]

# 120ms, 15.3MB
# 这里主要用的是 DP （动态规划）算法，然后逐步累加并取最小值，然后累加到最后就是最小的路径。

#=====================================================================================================#