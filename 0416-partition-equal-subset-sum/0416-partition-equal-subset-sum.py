class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if (total % 2 != 0) :
            return False
        dp = [[-1] * (half+1) for i in range(len(nums))]
        def fun(ind , target) :
            if (ind == 0) :
                if (nums[0] == target) :
                    return True
                else :
                    return False
            if (target == 0) :
                return True
            
            if (dp[ind][target] != -1) :
                return dp[ind][target]
            
            not_take = fun(ind - 1 , target)
            take = False
            if (target > nums[ind]) :
                take = fun(ind - 1 , target - nums[ind])

            dp[ind][target] = take or not_take
            return dp[ind][target]
        
        return fun(len(nums)-1 , half)