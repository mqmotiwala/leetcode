#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        my_set = set()
        while n not in my_set:
            my_set.add(n)
            s = str(n)
            sum = 0
            for c in s:
                sum += int(c)**2
            if sum == 1:
                return True
            
            n = sum
            print(n)
        
        return False

# @lc code=end

