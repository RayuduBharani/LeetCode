class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[0] * 2 for i in range(len(prices)+1)]

        for ind in range(len(prices)-1 , -1 , -1) :
            for buy in range(2) :
                profit = 0
                if (buy == 1) :
                    b = -prices[ind] + dp[ind+1][0]
                    not_buy = 0 + dp[ind + 1][1]
                    profit = max(b , not_buy)
                else :
                    sell = prices[ind] + dp[ind+1][1]
                    not_sell = 0 + dp[ind + 1][0]
                    profit = max(sell , not_sell)

                dp[ind][buy] = profit
        
        return dp[0][1]