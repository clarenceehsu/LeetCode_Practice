"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

#=====================================================================================================#

# First
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        nums.append('a')
        count = 0
        a = len(nums)
        if not nums:
            return 0
        while True:
            if count + 1 == a:
                break
            for n in range(count + 1, a):
                if nums[n] != nums[n - 1]:
                    count = count + 1
                else:
                    del nums[n]
                    a = a - 1
                    break
        return count

# 76ms,14.1MB
# 就是从第二个开始与前面一个相比较，如果相同就把后面的那个去掉，然后重新开始。
# 我的算法因为不管数据集是什么，一直都缺少最后一个数字，所以我索性在一开始就加上一个字母作为炮灰。

#=====================================================================================================#

# Second
class Solution(object):
    def removeDuplicates(self, nums):
        if nums == []: return 0
        left = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[left]:
                if left + 1 < i:
                    nums[left+1] = nums[i]
                left += 1
        del nums[left+1:]
        return len(nums)

# 56ms, 14MB
# 和前面的方法有异曲同工之妙，即将匹配到不同的数字与前面的进行一个调换，然后最后再一次性删掉后面的。

#=====================================================================================================#