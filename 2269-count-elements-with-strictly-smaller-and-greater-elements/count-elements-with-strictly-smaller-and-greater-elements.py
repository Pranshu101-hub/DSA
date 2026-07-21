class Solution:
    def countElements(self, nums: List[int]) -> int:
        if min(nums) == max(nums): return len(nums) - nums.count(min(nums))
        return len(nums) - nums.count(min(nums)) - nums.count(max(nums))