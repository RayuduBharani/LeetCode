class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        ans = float("-inf")
        ans = max(ans ,nums[0] * nums[1] * nums[2])
        ans = max(ans , nums[0] * nums[1] * nums[-1])
        ans = max(ans , nums[-1] * nums[-2] * nums[0])

        ans = max(ans , nums[-3] * nums[-2] * nums[-1])
    
        return ans