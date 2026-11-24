class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        if (amount == 0) :
            return 0
        dp = [[-1] * (amount + 1) for i in range(len(coins))]
        def fun(ind , amount) :
            if (ind == 0) :
                if (amount % coins[ind] == 0) :
                    return amount // coins[ind]
                else :
                    return float("inf")
            if (dp[ind][amount] != -1) :
                return dp[ind][amount]
            not_take = 0 + fun(ind - 1 , amount)
            take = float("inf")
            if (amount >= coins[ind]) :
                take = 1 + fun(ind , amount - coins[ind])
            dp[ind][amount] = min(take , not_take)
            return dp[ind][amount]
        
        a = fun(len(coins)-1 , amount)
        if a != float("inf") :
            return a
        return -1
