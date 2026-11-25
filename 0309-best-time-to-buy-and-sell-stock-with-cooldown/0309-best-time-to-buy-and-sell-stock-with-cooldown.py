class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[-1] * 2 for i in range(len(prices))]
        def fun(ind,buy) :
            if (len(prices) <= ind) :
                return 0
            if (dp[ind][buy] != -1) :
                return dp[ind][buy]
            if (buy == 1) :
                b = -prices[ind] + fun(ind+1 , 0)
                nb = 0 + fun(ind+1 , 1)
                profit = max(b , nb)
            else :
                s = prices[ind] + fun(ind+2 , 1)
                ns = 0 + fun(ind+1 , 0)
                profit = max(s,ns)
            
            dp[ind][buy] = profit
            return dp[ind][buy]
        return fun(0 , 1)