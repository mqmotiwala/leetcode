#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7
#

# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        string = ""
        if num < 0: 
            num = -num
            negative = True
        else:
            negative = False

        # edge case handling
        if num == 0:
            return "0"
        
        while num > 0:
            r = num%7
            num = num//7
            string = str(r) + string
        
        if negative:
            return('-'+string)
        else:
            return string
        
# @lc code=end