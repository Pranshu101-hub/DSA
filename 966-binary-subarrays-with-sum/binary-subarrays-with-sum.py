class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0: 1}
        sum = 0
        tot = 0
        
        for i in nums:
            sum += i
            if sum - goal in d:
                tot += d[sum - goal]
            d[sum] = d.get(sum, 0) + 1

        return tot