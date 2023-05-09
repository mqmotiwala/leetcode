#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t):
            s_map = {}
            t_map = {}
            for i in range(len(s)):
                s_map[s[i]] = s_map.get(s[i], 0) + 1
                t_map[t[i]] = t_map.get(t[i], 0) + 1
            
            return True if s_map == t_map else False
        else:
            return False

        
# @lc code=end

