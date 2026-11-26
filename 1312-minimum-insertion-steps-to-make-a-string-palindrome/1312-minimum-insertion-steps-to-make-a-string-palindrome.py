class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        m = len(s)
        n = len(s1)
        dp = [[-1] * n for i in range(m)]
        def fun(i , j) :
            if (i < 0 or j < 0) :
                return 0
            if (dp[i][j] != -1) :
                return dp[i][j]
            if (s[i] == s1[j]) :
                dp[i][j] = 1 + fun(i-1 , j-1)
            else :
                dp[i][j] = max(fun(i , j-1) , fun(i-1 , j))
            return dp[i][j]
        
        ans = fun(m-1 , n-1)
        return len(s1) - ans