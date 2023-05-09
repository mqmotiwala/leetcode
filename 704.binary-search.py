#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        
# @lc code=end

