class Solution:
    def totalFruit(self, arr: list[int]) -> int:
        k = 2

        dicci = {}
        l = 0
        ans = 0
        for i in range(len(arr)) :
            if (arr[i] in dicci) :
                dicci[arr[i]] += 1
            else :
                dicci[arr[i]] = 1

            while len(dicci) > k :
                dicci[arr[l]] -= 1
                if (dicci[arr[l]] == 0) :
                    del dicci[arr[l]]
                l += 1

            ans = max(ans , i - l + 1)
        return ans