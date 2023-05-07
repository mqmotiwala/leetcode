#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            return 0 if haystack==needle else -1
        else:
            for i in range(len(haystack)):
                print(haystack[i:i+len(needle)], needle)
                if i+len(needle) <= len(haystack) and haystack[i:i+len(needle)] == needle:
                    return i
            return -1
    
# @lc code=end