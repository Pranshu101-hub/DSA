class Solution:
    def jump(self, nums: List[int]) -> bool:
        maxi = 0
        c = 0
        l,r = 0,1
        while r < len(nums):
            print(l,r,c,maxi)
            for i in range(l,r):
                maxi = max(nums[i]+i+1, maxi)
            c += 1
            l = r
            r = maxi
        return c