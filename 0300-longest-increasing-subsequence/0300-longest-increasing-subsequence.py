class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for ind in range(len(nums)) :
            for prev in range(ind + 1) :
                if (nums[ind] > nums[prev]) :
                    dp[ind] = max(1 + dp[prev] , dp[ind])
        
        return max(dp)