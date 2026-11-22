class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for i in range(m)]
        
        def fun(i , j) :
            if (i == 0 and j == 0 and obstacleGrid[i][j] == 0)  :
                return 1
            if (i < 0 or j < 0 or obstacleGrid[i][j] == 1) :
                return 0
            
            if (dp[i][j] != -1) :
                return dp[i][j]
            
            up = fun(i , j -1)
            left = fun(i-1 , j)

            dp[i][j] = up + left 
            return dp[i][j]

        return fun(m-1 , n-1) 