class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        su = 0
        maxx = float('-inf')
        for i in range(len(nums)):
            if su<0 :
                su = 0
            su += nums[i]
            maxx = max(su,maxx)
        return maxx
            
            