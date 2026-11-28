class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        currentMin = float('inf')
        for i in range(len(prices)):
            if prices[i] < currentMin:
                currentMin = prices[i]
            profit = prices[i]-currentMin
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit