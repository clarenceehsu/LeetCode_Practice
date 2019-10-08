'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

#=====================================================================================================#

# First


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    	S, d, i, j, m = [[0]*n for i in range(n)], [0,1,0,-1], 0, 0, 0
    	for k in range(1,n*n+1):
    		S[i][j], a, b = k, i + d[m % 4], j + d[(m + 1) % 4]
    		if a in [-1,n] or b in [-1,n] or S[a][b] != 0: m +=  1
    		i, j = i + d[m % 4], j + d[(m + 1) % 4]
    	return S

# 32ms, 13.9MB
# 那个 d 是行列的步长，行取 0 的时候，列取 1， 即行不动，列加 1 加到最右边，然后 m += 1；
# 这个时候的行取 1，列取 0，所以列不变，行加 1，往下走走到底，然后 m += 1；
# 然后行取 0，列取 1 这样往来重复。
# 当指针到的数组值不为 0 的时候提前 m += 1，从而完成缩减的操作。

#=====================================================================================================#