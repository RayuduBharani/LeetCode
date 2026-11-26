class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for i in range(len(text1)+1)]
        for ind1 in range(1 , len(text1)+1) :
            for ind2 in range(1 ,len(text2)+1) :
                if (text1[ind1-1] == text2[ind2-1]) :
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else :
                    dp[ind1][ind2] = max(dp[ind1-1][ind2] , dp[ind1][ind2-1])

        print(dp)
        return dp[len(text1)][len(text2)]