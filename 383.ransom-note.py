#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_hash, mag_hash = {}, {}

        if len(magazine) < len(ransomNote):
            return False

        # build ransom_hash
        for letter in ransomNote:
            ransom_hash[letter] = ransom_hash.get(letter, 0) + 1
        
        # build mag_hash
        for letter in magazine:
            mag_hash[letter] = mag_hash.get(letter, 0) + 1

        # check for sufficiency
        for letter, count in ransom_hash.items():
            if not (letter in mag_hash and mag_hash[letter] >= count):
                return False
        
        return True

        
# @lc code=end

