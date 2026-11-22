class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for i in range(m)]
        def fun(i , j) :
            if (i < 0 or j < 0) :
                return float("inf")
            if (i == 0 and j == 0) :
                return grid[i][j]
            if (dp[i][j] != -1) :
                return dp[i][j]
            up = fun(i , j - 1) + grid[i][j]
            left = fun(i-1 , j) + grid[i][j]

            dp[i][j] = min(up , left)

            return dp[i][j]
        
        return fun(m-1 , n-1)