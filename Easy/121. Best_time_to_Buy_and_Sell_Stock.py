# Pattern: Greedy / Sliding Window
# Time: O(n) | Space: O(1)
# Key insight: track minimum price seen so far
# at each step calculate profit vs current min
# no need to check every pair — O(n) not O(n²)

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
