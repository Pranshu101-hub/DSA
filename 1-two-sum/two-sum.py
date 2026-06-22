class Solution:
    def twoSum(self, nums, target):
        res = []

        for i in range(len(nums)):
            if target - nums[i] in nums:
                if ((target - nums[i])*2 == target and nums.count(target - nums[i]) == 2) or(target - nums[i])*2 != target:
                    res.append(i)
                    break

        for j in range(len(nums)):
            if target - nums[i] == nums[j] and i != j:
                res.append(j)
                break
        
        return res