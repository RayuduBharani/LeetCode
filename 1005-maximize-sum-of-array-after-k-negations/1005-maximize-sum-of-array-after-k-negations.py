class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)) :
            if (k <= 0) :
                return sum(nums)  
            if (nums[i] < 0) :
                nums[i] = (nums[i] * -1)
                k -= 1
        print(nums , k)
        
        if (k % 2 != 0) :
            nums.sort()
            nums[0] *= -1
            
        return sum(nums)