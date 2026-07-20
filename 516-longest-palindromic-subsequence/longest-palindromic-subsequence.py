class Solution(object):
    def longestPalindromeSubseq(self, s):
        n=len(s)
        s1 = s[::-1]
        dp = [[None]*(n+1) for _ in range(1+n)]
        for i in range(n+1):
            dp[0][i] = 0
            dp[i][0] = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1] == s[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]