#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        
        return (m if nums[m] > target else m+1)
        

        
# @lc code=end

