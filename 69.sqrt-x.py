#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        l = 0
        r = x
        while l <= r:
            m = (l+r)//2
            square = m*m
            if square < x:
                l = m+1
                res = m
            elif square > x:
                r = m-1
            else:
                # if m**2 == x
                return(m)

        return(res)

# @lc code=end