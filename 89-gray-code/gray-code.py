class Solution:
    def grayCode(self, n: int) -> List[int]:
        l = []
        tot = 1 << n
        for i in range(tot):
            l.append(i^(i>>1))
        return l