class Solution:
    def coinChange(self, coins: list[int], m: int) -> int:
        def minNone(a,b):
            if a is None: return b
            elif b is None: return a
            else: return min(a,b)
        if m == 0: return 0
        dp = [None]*(m+1)
        dp[0] = 0
        #print(dp)
        for i in range(1,m+1):
            if i in coins: dp[i] = 1
            else:
                for c in coins:
                    if i-c < 0: continue
                    try:
                        dp[i] = minNone(dp[i],dp[i-c]+1)
                    except: continue
            #print(dp)
        if dp[-1]:
            return dp[-1]
        return -1