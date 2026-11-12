class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        l = 0
        for i in range(1 , len(nums)) :
            if (nums[i] == nums[l]) :
                nums[i] = nums[i] + 1
                ans += 1
            elif (nums[i] <= nums[l]) :
                ans += (nums[l] + 1) - nums[i]
                nums[i] = nums[l] + 1
            l += 1
        return ans