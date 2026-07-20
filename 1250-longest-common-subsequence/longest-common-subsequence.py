class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n,m = len(s1),len(s2)
        dp = [[None]*(n+1) for i in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 0
        for j in range(m+1):
            dp[j][0] = 0
        #print(dp)
        for i in range(1,m+1):
            #print('debug')
            for j in range(1,n+1):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else: 
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                #print('-')
                #print(dp)
        return dp[-1][-1]