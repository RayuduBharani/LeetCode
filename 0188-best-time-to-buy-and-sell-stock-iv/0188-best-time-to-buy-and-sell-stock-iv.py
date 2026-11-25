class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp = [[[-1] * (k+1) for _ in range(3)] for _ in range(len(prices))]

        def fun(ind , buy , cap) :
            if (cap == 0) :
                return 0
            if (ind == len(prices)) :
                return 0
            if (dp[ind][buy][cap] != -1) :
                return dp[ind][buy][cap]
            profit = 0
            if (buy == 1) :
                b = -prices[ind] + fun(ind +1 , 0 , cap)
                nb = 0 + fun(ind +1 , 1 , cap)
                profit = max(b , nb)
            else :
                s = prices[ind] + fun(ind+1 , 1 , cap - 1)
                ns = 0 + fun(ind + 1 , 0 , cap)
                profit = max(s , ns)
            dp[ind][buy][cap] = profit
            return dp[ind][buy][cap]
        
        return fun(0 , 1 , k)