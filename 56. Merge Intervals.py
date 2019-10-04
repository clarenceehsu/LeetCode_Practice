'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

#=====================================================================================================#

# First


class Solution:
    def merge(self, intervals):
            if not intervals: return []
            intervals = sorted(intervals, key = lambda x: x[0])
            l, r = intervals[0]
            res = []
            for i in range(1, len(intervals)):
                cl, cr = intervals[i]
                if r < cl:
                    res.append([l, r])
                    l, r = cl, cr
                else:
                    r = max(r, cr)
            res.append([l, r])
            return res

# 88ms, 15.7MB
# 算法的代码很直观。

#=====================================================================================================#