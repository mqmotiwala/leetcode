#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        # the solution below uses a dict to hold str_map,
        # but the same can be done via an arr using ord() function
        result = {}

        for str in strs:
            # count is an array of 26 elements 
            # use ord() to get the position of each letter
            count = [0]*26
            for c in str:
                count[ord(c)-ord("a")] += 1

            if not tuple(count) in result:
                result[tuple(count)] = []
            
            result[tuple(count)].append(str)

        return(result.values())

        # this solution uses a dict to hold str_map
        # result = {}

        # # build an alphabet dict 
        # # each word will have a count of its individual letters and 0 elsewhere
        # # this is required to ensure all letters are sequential
        # alphabets = "abcdefghijklmnopqrstuvwxyz"
        # for str in strs:
        #     str_map = {c:0 for c in alphabets}
        #     for letter in str:
        #         str_map[letter] += 1
            
        #     # only immutable objects can be keys
        #     # therefore, convert map to tuple to use in result
        #     str_map = tuple(str_map.items())
        #     if not str_map in result:
        #         # initialize array, if not already exist
        #         result[str_map] = []
        #     result[str_map].append(str)
        
        # return(result.values())

# @lc code=end