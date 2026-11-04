class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [-1] * len(nums)
        l = 0
        summ = 0
        window = 2 * k + 1
        for i in range(len(nums)) :
            summ += nums[i]
            if (i - l + 1 > window) :
                summ -= nums[l]
                l += 1
            if (i - l + 1 == window) :
                print(summ , window)
                ans[i-k] = (summ // window)

        return ans