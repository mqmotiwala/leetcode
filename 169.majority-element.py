#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        # time complexity = n*log(n)
        majority_threshold = len(nums)/2.0

        nums.sort()
        prev_val = 0
        count = 0
        for num in nums:
            if num != prev_val:
                prev_val = num
                count = 1
            else:
                count += 1
            
            if count >= majority_threshold:
                return(num)
        
# @lc code=end
