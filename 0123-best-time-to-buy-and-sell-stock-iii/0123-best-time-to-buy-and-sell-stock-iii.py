class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[[-1] * (3) for _ in range(2)] for i in range(len(prices)+1)]
        def fun(ind , buy , cap) :
            if (len(prices) == ind) :
                return 0
            if (cap == 0) :
                return 0
            if (dp[ind][buy][cap] != -1) :
                return dp[ind][buy][cap]
            profit  = 0
            if (buy == 1) :
                b = -prices[ind] + fun(ind+1 , 0 , cap)
                not_b = 0 + fun(ind+1 , 1 , cap)
                profit = max(b , not_b)
            else :
                s = prices[ind] + fun(ind+1 , 1 , cap - 1)
                not_s = 0 + fun(ind+1 , 0 , cap)
                profit = max(s , not_s)
            
            dp[ind][buy][cap] = profit
            return dp[ind][buy][cap] 
        return fun(0 , 1 , 2)