#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        triangle = []

        # build row 0 of triangle
        triangle.append([1])

        for row in range(1, numRows):
            row_arr = []
            for cell in range(row+1):
                val_1 = triangle[row-1][cell-1] if 0<=cell-1<len(triangle[row-1]) else 0
                val_2 = triangle[row-1][cell] if 0<=cell<len(triangle[row-1]) else 0
                row_arr.append(val_1 + val_2)
            
            triangle.append(row_arr)
        
        return(triangle)
        
# @lc code=end