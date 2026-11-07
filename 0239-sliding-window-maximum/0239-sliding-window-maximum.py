from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = 0
        dq = deque()
        ans = []
        for i in range(len(nums)) :
            # if (len(dq) == 0 or (nums[dq[-1]] < nums[i])) :
            #     dq.append(i)
            # else :
            while (dq and nums[dq[-1]] < nums[i]) :
                dq.pop()
            dq.append(i)
            
            if (i - l + 1 > k) :
                if dq[0] == l:
                    dq.popleft()
                l += 1
            
            if (i - l + 1 == k) :
                ans.append(nums[dq[0]])
        return ans