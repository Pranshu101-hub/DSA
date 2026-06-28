class Solution(object):
    def canPartition(self, nums):
        su = sum(nums)
        if su % 2: return False
        tar = su // 2
        dp = [False] * (tar + 1)
        dp[0] = True
        for i in nums:
            for j in range(tar, i-1, -1):
                dp[j] = dp[j] or dp[j - i]
        return dp[tar]