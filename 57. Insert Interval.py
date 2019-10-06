'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

#=====================================================================================================#

# First


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])

        return result

# 92ms, 17.4MB
# 算法比较简单，就是添加之后再排序，然后再按照上题的算法合并。

#=====================================================================================================#