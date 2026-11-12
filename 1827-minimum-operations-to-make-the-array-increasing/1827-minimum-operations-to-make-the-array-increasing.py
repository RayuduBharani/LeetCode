class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        for i in range(1,len(nums)) :
            if (nums[i] <= nums[l]) :
                ans += (nums[l] + 1) - nums[i]
                nums[i] = nums[l] + 1
            l += 1
        return ans