'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

#=====================================================================================================#

# First


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        indices = list(range(k))
        result = []
        while True:
            result.append([i+1 for i in indices])

            # Find the last index that can be incremented:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break
            else: # If no index can be incremented, we've seen the final combination:
                return result

            # Increment that index and push all subsequent indices to the left:
            indices[i] += 1
            for j in range(i+1, k):
                indices[j] = indices[j-1] + 1

# 80 ms, 15.1 MB
# 这个解法的原理和 collection 的一样，知识简化了一些。

#=====================================================================================================#

# Second


from itertools import combinations as cs

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return cs(range(1, n + 1), k)

# 76 ms, 14.5 MB
# 一行大法好。