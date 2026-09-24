class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # If the starting cell has an obstacle, no paths are possible
        if obstacleGrid[0][0] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 1D DP array to store the number of paths for the current row
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # If there's an obstacle, paths to this cell drop to 0
                    dp[j] = 0
                elif j > 0:
                    # Otherwise, paths = paths from above (current dp[j]) 
                    # + paths from the left (dp[j-1])
                    dp[j] += dp[j-1]
                    
        return dp[-1]