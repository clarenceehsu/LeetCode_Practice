'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

#=====================================================================================================#

# First


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(queens, ijDiff, ijSum):
            p = len(queens)   # depth, row index
            if p == n:
                res.append(queens)
                return None
            for q in range(n):   # label, column index
                if q not in queens and p-q not in ijDiff and p+q not in ijSum:
                    helper(queens+[q], ijDiff+[p-q], ijSum+[p+q])
        res = []
        helper([], [], [])
        return [['.'*j + 'Q' + '.'*(n-j-1) for j in solution] for solution in res]

# 60ms, 14.4MB
# 这道题我以前的想法是先建立一个列表，把满足的点定为 Q，其余的点定为 .，然后用 DFS 算法遍历出来。
# 后来我发现这样写十分麻烦，然后参考了别人的算法，是去一行行生成这些满足条件的行，然后最后生成出来。

#=====================================================================================================#