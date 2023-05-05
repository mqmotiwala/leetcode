#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        int_value = {
           'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000 
        }

        ## PSEUDOCODE
        # you're at the beginning
            # look at the next, see if edge case applies
                # if it applies, do next-curr
                # if not, do curr
        # you're in the middle 
            # check if curr is greater than last
                # if yes, skip
                # if not, 
                    # look at the next, see if edge case applies
                        # if it applies, do next-curr
                        # if not, do curr
        # you're at the end
            # check if curr is greater than last
                # if yes, skip
                # if not, # do curr

        answer = 0 
        for i in range(len(s)):
            if len(s) == 1:
                answer += int_value[s[i]]
            elif i == 0:
                if int_value[s[i+1]] > int_value[s[i]]:
                    answer += int_value[s[i+1]] - int_value[s[i]]
                else:
                    answer += int_value[s[i]]
            elif i+1 != len(s):
                if int_value[s[i-1]] < int_value[s[i]]:
                    continue
                elif int_value[s[i+1]] > int_value[s[i]]:
                    answer += int_value[s[i+1]] - int_value[s[i]]
                else:
                    answer += int_value[s[i]]
            elif i+1 == len(s):
                if int_value[s[i-1]] < int_value[s[i]]:
                    continue
                else:
                    answer += int_value[s[i]]

        return answer

# @lc code=end