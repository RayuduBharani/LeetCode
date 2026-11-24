class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[-1] * (amount + 1) for i in range(len(coins))]
        def fun(ind , amount) :
            if (ind == 0) :
                if (coins[ind] >= 1 and amount % coins[ind] == 0) :
                    return 1
                else :
                    return 0
            if (dp[ind][amount] != -1) :
                return dp[ind][amount]
            not_take = fun(ind-1 , amount)
            take = 0
            if (coins[ind] <= amount) :
                take = fun(ind , amount - coins[ind])
            
            dp[ind][amount] = take + not_take
            return dp[ind][amount] 
        
        return fun(len(coins)-1 , amount)