class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, profit = 0, 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            elif prices[right] > prices[left]:
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]
        return profit  