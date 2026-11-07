class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        summ = 0
        ans = float("inf")
        for i in range(len(nums)) :
            summ += nums[i]
            while summ >= target :
                ans = min(ans , i - l+1)
                summ -= nums[l]
                l += 1
        if (ans == float("inf")) :
            return 0
        return ans