'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

#=====================================================================================================#

# First


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.res = 0
        self.n = n
        self.helper([], [], [])
        return self.res
        
    def helper(self, queens, ijDiff, ijSum):
        p = len(queens)
        if p == self.n:
            self.res += 1
            return None
        for q in range(self.n):   # label, column index
            if q not in queens and p-q not in ijDiff and p+q not in ijSum:
                self.helper(queens+[q], ijDiff+[p-q], ijSum+[p+q])

# 52ms, 13.8MB
# 算法和上题一样，都是用的 DFS 算法遍历出所有的结果（毕竟不变里出来的话是不知道有没有的，所以还是要遍历）
# 只是把输出和中间的运算过程化简了一下

#=====================================================================================================#