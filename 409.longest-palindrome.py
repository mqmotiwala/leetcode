#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        # the idea is to build a hashmap of count of letters
        # all even values can be used readily
        # odd values can only be used if they are 3 or more, 
            # i.e. for 'ccc', 2 c's can be used readily
        # there is always room for 1 odd letter in the center of the palindrome
            # so, you either use the 3rd letter of a 3-count letter
            # or any other 1-count letter

        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        res = 0
        odd_carry = False
        for val in s_map.values():
            if val%2 == 0:
                res += val
            elif val%2 == 1:
                res += val-1
                odd_carry = True
        
        return res+1 if odd_carry else res

# @lc code=end