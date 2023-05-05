#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        n = nums[0]
        for num in nums:
            if num > n:
                nums[k] = num
                n = num
                k += 1
        
        return k
        
# @lc code=end

