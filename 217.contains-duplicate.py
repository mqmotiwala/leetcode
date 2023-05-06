#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        hash = {}
        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = 1

        return False
        
# @lc code=end

