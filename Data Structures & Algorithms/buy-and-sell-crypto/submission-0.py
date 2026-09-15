class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0

        for i in range(1, len(prices)):
            minp = min(minp, prices[i])
            currp = prices[i] - minp
            maxp = max(maxp, currp)
        return maxp