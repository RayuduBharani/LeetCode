class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for i in range(len(text1))]
        def fun(ind1 , ind2) :
            if (ind1 < 0 or ind2 < 0) :
                return 0
            if (dp[ind1][ind2] != -1) :
                return dp[ind1][ind2]
            if (text1[ind1] == text2[ind2]) :
                return 1 + fun(ind1-1 , ind2-1)
            dp[ind1][ind2] = max(fun(ind1-1 , ind2) , fun(ind1 , ind2-1))
            return dp[ind1][ind2]
        return fun(len(text1)-1 , len(text2)-1)