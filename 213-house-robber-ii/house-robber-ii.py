class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums ) == 2:
                return max(nums[1],nums[0])
            dp = [0] * (len(nums)+1)
            dp[1] = nums[0]
            for i in range(2,len(dp)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
                print(dp)
            return dp[-1]
        if len(nums) == 1:
                return nums[0]
        if len(nums ) == 2:
            return max(nums[1],nums[0])
        return max(f(nums[1:]),f(nums[:-1]))