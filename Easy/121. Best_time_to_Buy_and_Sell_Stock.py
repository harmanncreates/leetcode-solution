class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices [0]
        max_profit = 0
        for price in prices:
            if price < cheapest:
                cheapest = price
            profit = price - cheapest
            if profit > max_profit:
                max_profit = profit
        return max_profit
