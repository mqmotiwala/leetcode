#
# @lc app=leetcode id=824 lang=python
#
# [824] Goat Latin
#

# @lc code=start
class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = 'aeiou'

        output = ''
        for i, word in enumerate(sentence.split()):
            if not word[0].lower() in vowels:
                word = word[1:] + word[0]
            
            output += word + 'ma' + 'a'*(i+1) + ' '
        
        # strip final empty space from the string
        return(output[:-1])
        
# @lc code=end