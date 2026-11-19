class Solution:
    def rob(self, arr: list[int]) -> int:
        dp = [0] * len(arr)
        for ind in range(len(arr)) :
            take = arr[ind]
            if (ind > 1) :
                take = dp[ind-2] + arr[ind] 
            not_take = dp[ind-1] + 0
            
            dp[ind] = max(take , not_take)
            
        return dp[-1]