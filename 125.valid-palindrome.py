#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()

        copy = s
        for c in copy:
            if c not in allowed_chars:
                s = s.replace(c, '')
        
        return True if s == s[::-1] else False
        
# @lc code=end