#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        # non-pythonic solution
        i = len(s) - 1

        while s[i] == ' ':
            # skip whitespace at the end if exists
            i -= 1
        
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length         

        # # pythonic solution
        # return (len(s.split()[-1]))
        
# @lc code=end
