class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minn = float("inf")
        ans = float("-inf")

        for i in range(len(prices)) :
            print(minn)
            minn = min(minn , prices[i])
            ans = max(ans , (prices[i]-minn))
            print(ans , "a")
        return ans