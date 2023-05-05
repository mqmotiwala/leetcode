#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        lookup = {
            '(':')',
            '{':'}',
            '[':']'
        }

        opens = 0
        expected_closer = []
        for c in s:
            if c in lookup:
                # its an opener
                opens += 1
                # add next expected closer to the end of the list
                expected_closer.append(lookup[c])
            else:
                # its a closer
                if expected_closer and c == expected_closer[-1]:
                    # if expected_closer list is non empty
                    # then the last item in list = the expected closer
                    opens -= 1
                    # use .pop() to remove last item,
                    # this sets the expected closer to the new last item
                    expected_closer.pop()
                else:
                    # unexpected closer
                    return False
        
        if opens == 0:
            # all opens have been closed
            return True
        else:
            # unclosed opens exist
            return False
        
# @lc code=end