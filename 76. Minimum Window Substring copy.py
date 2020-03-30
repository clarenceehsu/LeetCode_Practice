'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

#=====================================================================================================#

# First


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = dict(collections.Counter(t)) 
        
        
        formed = 0
        slow  = 0
        
        
        min_str = None
        min_length = sys.maxsize - 1
        
        
        for fast in range(len(s)):
            
            """
            skip if s[fast] doesn't matter
            """
            ch = s[fast]
            fast += 1
            if ch not in d:
                continue
            
            """
            use the ch to update d
            """
            d[ch] -= 1
            if d[ch] == 0:
                formed  += 1
            
            
            """
            If all character are satisfied, then need to move the left pointer
            """
            while formed == len(d) and slow <= fast:
                
                """
                save the result
                """
                curr_length = fast - slow
                if curr_length < min_length:
                    min_length = curr_length
                    min_str = s[slow:fast]
                
                
                
                """
                update the left boundary
                """
                ch = s[slow]
                slow += 1
                if ch not in d: 
                    continue
                d[ch] += 1
                if d[ch] == 1:
                    formed -= 1
            
        return min_str if min_str is not None else ""

# 88 ms, 13.3 MB
# 用了 Slide Window 的解法，就是双指针，然后前一个一直往前，后一个在满足要求的情况下尽可能往前。
# 然后中间的就是满足条件的字符串，然后统计下来取最小值即可。

#=====================================================================================================#