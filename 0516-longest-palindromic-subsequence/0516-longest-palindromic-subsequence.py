class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s[::-1]
        dp = [[-1] * len(s1) for i in range(len(s))]
        def fun(i , j) :
            if (i < 0 or j < 0) :
                return 0
            if (dp[i][j] != -1) :
                return dp[i][j]
            if (s[i] == s1[j]) :
                dp[i][j] = 1 + fun(i - 1 , j - 1)
            else :
                dp[i][j] = max(fun(i-1,j) , fun(i , j -1))
            return dp[i][j]
        
        return fun(len(s)-1 , len(s1)-1)