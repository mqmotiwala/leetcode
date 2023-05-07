#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        # non-hacky solution
        carry = 1
        i = len(digits) - 1

        while carry == 1:
            if digits[i] != 9:
                digits[i] += 1
                carry = 0
            else:
                # digits[i] == 9
                if i != 0:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] = 0
                    digits.insert(0,1)   
                    carry = 0             
        
        return(digits)
        
        ## hacky solution... 
        # if digits[-1] != 9:
        #     digits[-1] += 1
        #     return (digits)
        # else:
        #     s = ''
        #     for n in digits:
        #         s += str(n)
        #     s = int(s)
        #     s += 1
        #     s = str(s)
        #     digits = []
        #     for c in s:
        #         digits.append(int(c))
        #     return(digits)
        
# @lc code=end