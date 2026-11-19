class Solution:
    def rob(self, nums: list[int]) -> int:
        if (len(nums) == 1) :
            return nums[0] 
        dp = [-1] * len(nums)
        def fun(nums , ind) :
            if (ind < 0) :
                return 0
            if (ind == 0) :
                return nums[ind]
            if (dp[ind] != -1) :
                return dp[ind]
            not_take = 0 + fun(nums , ind - 1)
            take = nums[ind] + fun(nums , ind - 2)
            dp[ind] = max(take , not_take)
            return dp[ind]

        a = fun(nums[:-1], len(nums[:-1]) - 1)

        dp = [-1] * len(nums)

        b = fun(nums[1:], len(nums[1:]) - 1)

        return max(a, b)