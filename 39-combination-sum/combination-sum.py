class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        return self.pick(0, target, [], cand, [])

    def pick(self, i, t, arr, cand, res):
        if i == len(cand) or t<0:
            return
        if t == 0 and arr not in res:
            res.append(arr)
        self.pick(i, t-cand[i], arr+[cand[i]], cand, res)
        self.pick(i+1, t, arr, cand, res)
        return res