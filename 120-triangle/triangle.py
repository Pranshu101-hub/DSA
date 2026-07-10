class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0]*(i+1) for i in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1,m):
            n = len(triangle[i])
            for j in range(n):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == n-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        print(dp)
        return min(dp[-1])
