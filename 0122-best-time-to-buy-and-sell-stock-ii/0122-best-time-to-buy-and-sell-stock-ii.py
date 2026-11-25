class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[-1] * 2 for i in range(len(prices))]
        def fun(ind , buy) :
            if (ind == len(prices)) :
                return 0
            profit = 0

            if (dp[ind][buy] != -1) :
                return dp[ind][buy]
            
            if (buy == 1) :
                b = -prices[ind] + fun(ind+1 , 0)
                not_buy = 0 + fun(ind + 1 , 1)
                profit = max(b , not_buy)
            else :
                sell = prices[ind] + fun(ind+1 , 1)
                not_sell = 0 + fun(ind + 1 , 0)
                profit = max(sell , not_sell)

            dp[ind][buy] = profit
            return dp[ind][buy]
        
        return fun(0 , 1)