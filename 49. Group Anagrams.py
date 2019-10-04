'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

#=====================================================================================================#

# First


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            h = 1
            for c in x:
                h += hash(c)
            if h not in dic:
                dic[h] = []
            dic[h].append(x)
        return list(dic.values())

# 104ms, 16.9MB
# 用哈希值，把每一个字符串拆开来计算hash然后相加，所以只要有相同的数字就会有相同的哈希值。

#=====================================================================================================#