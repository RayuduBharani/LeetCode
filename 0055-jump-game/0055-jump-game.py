class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxx = 0
        for i in range(len(nums)) :
            if (i > maxx) :
                return False
            maxx = max(maxx , nums[i] + i)
        return True