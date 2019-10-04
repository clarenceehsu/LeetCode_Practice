'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

#=====================================================================================================#

# First


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        start_row = start_col = 0
        end_row = len(matrix)-1
        end_col = len(matrix[0])-1
        num = 0
        
        if start_row == end_row or start_col == end_col:
            return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
		
        while start_col <= end_col and start_row <= end_row:
            ## up
            for i in range(start_col,end_col+1):
                res.append(matrix[start_row][i])
            start_row += 1
            
            # right
            for j in range(start_row,end_row+1):
                res.append(matrix[j][end_col])
            end_col -= 1
             # down 
            if start_row <= end_row:
                for m in range(end_col,start_col-1,-1): 
                    res.append(matrix[end_row][m])
            end_row -= 1 
            # left
            if start_col <= end_col:
                for n in range(end_row,start_row-1,-1):
                    res.append(matrix[n][start_col])
            start_col += 1

        return res

# 32ms, 13.5MB
# 这个的算法就很简单了，跑个圈。

#=====================================================================================================#