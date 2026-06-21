class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl' , '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        if digits == '': return []
        self.f(digits, 0 ,d,'',res)
        return res
    def f(self, nums, i, d, p, res):
        if i >=len(nums):
            res.append(p)
            return
        string1 = d[nums[i]]
        for j in string1:
            self.f(nums, i+1, d, p + j, res)
