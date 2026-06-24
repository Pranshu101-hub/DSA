class Solution:
    def maxProfit(self, l: List[int]) -> int:
        maxp = float('-inf')
        store = float('inf')
        for i in l:
            store = min(i,store)
            maxp = max(maxp,i-store)
        return maxp
