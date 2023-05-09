#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        last_good = 0
        first_bad = n
        while last_good < first_bad:
            m = (last_good + first_bad)//2

            if isBadVersion(m):
                first_bad = m
            else:
                last_good = m

            if last_good + 1 == first_bad:
                return(first_bad)     
        
# @lc code=end

