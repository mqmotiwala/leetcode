#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        max_profit = 0
        for price in prices:
            if price < buy:
                buy = price
                continue
        
            if price-buy > max_profit:
                max_profit = price-buy
            
            # print(price, buy, price-buy, max_profit)
        
        return max_profit


        
# @lc code=end

Solution().maxProfit([7,1,5,3,6,4])
