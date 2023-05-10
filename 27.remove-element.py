#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        # edge case, nums has 1 element and its val
        if len(nums) == 1 and nums[0] == val:
            return(0)
        
        for i, num in enumerate(nums):
            if num == val:
                if i == len(nums)-1:
                    # you're at the end of the list
                    return(i)
                else:
                    # you're not at the end of the list
                    j = i + 1
                    while nums[j] == val:
                        if j == len(nums)-1:
                            # you have reached the end of nums
                            # so there is a direct repetition of val
                                # from i-1 element to end of nums
                                # therefore:
                                #   i-1 is the last non-val num, and
                                #   i is length of non-val nums
                            return(i)
                        j += 1
                    
                    # if this executes, you found a non-val num before end of array
                    # therefore, swap val at ith element with the non-val num found
                    nums[i] = nums[j]
                    nums[j] = val
        
        # if this executes, there must have been 0 vals in nums
        # therefore:
        return (len(nums))


        
# @lc code=end

