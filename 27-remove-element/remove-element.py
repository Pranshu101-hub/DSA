class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = len(nums)
        st = 0
        while st<len(nums):
            if nums[st] == val:
                c -= 1
                nums.pop(st)
                continue
            st += 1
        return c

