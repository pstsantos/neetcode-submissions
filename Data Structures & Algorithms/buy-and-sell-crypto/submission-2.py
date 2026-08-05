class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize left and right pts
        buyL, sellR = 0,1
        maxProfit = 0

        while sellR < len(prices):
            if prices[buyL] < prices[sellR]:
                profit = prices[sellR] - prices[buyL]
                maxProfit = max(maxProfit, profit)
            else:
                  buyL = sellR
            sellR += 1
        return maxProfit


