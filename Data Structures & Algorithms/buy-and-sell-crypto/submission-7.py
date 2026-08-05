#u -> input (prices[])
# pick the lowest ith to buy
# pick the higher ith to sell
# output (max diff between lo and hi)
# if no profit, return 0

#p ->
#two-pointer approach
#start a variable profit = 0 
#start a pointer buy = 0, sell = 1
# while profit is lower than sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 #ok
        buy, sell = 0, 1 #ok

        while sell < len(prices): 
            if prices[buy] < prices[sell]:
                currProfit = prices[sell] - prices[buy]
                maxProfit = max(currProfit, maxProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit
            
            

        