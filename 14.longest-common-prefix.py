#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        # n time complexity solution
        result = strs[0]
        for string in strs:
            if string == result:
                continue
            else:
                while result != string[:len(result)]:
                    result = result[:-1]        
        return result

        # n^2 time complexity solution
        # result = ""
        # # do as many loops as the minimum string length
        # for i in range(len(min(strs, key=len))):
        #     # set char to compare 
        #     c = strs[0][len(result)]
        #     for string in strs:
        #         if not string[i] == c:
        #             return result
            
        #     result += c
        # return result

# @lc code=end

