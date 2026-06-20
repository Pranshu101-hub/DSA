class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        pos = pos[::-1]
        neg = neg[::-1]
        for i in range(len(nums)):
            if not i%2:
                ans.append(pos.pop())
                
            else:
                ans.append(neg.pop())
                
        return ans