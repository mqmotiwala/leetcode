#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        map = {}
        for i, c in enumerate(s):
            if c not in map:
                if t[i] in map.values():
                    return False
                else:
                    map[c] = t[i]
                    continue
            if c in map and not map[c] == t[i]:
                return False
        return True

# @lc code=end