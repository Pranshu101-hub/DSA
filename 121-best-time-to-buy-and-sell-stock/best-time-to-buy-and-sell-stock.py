class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = -float('inf')
        minn = prices[0]
        for i in prices:
            maxp = max(i - minn, maxp)
            minn = min(i,minn)
        return maxp