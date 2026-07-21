class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                y = i+1
                while y in nums:
                    y+=1
                best = max(best,y-i)
        return best