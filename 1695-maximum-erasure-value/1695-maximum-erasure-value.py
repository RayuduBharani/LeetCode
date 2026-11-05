class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        l = 0
        sett = set()
        summ = 0
        ans = 0
        for i in range(len(nums)) :
            summ += nums[i]
            if (nums[i] not in sett):
                sett.add(nums[i])
            else :
                while nums[i] in sett :
                    summ -= nums[l]
                    sett.remove(nums[l])
                    l += 1
                sett.add(nums[i])
            ans = max(ans , summ)
        return ans