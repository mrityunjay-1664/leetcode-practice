class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
            # Update the lowest price seen so far
                min_price = price
            elif price - min_price > max_profit:
            # Calculate profit if we sold at current price and update max_profit
                max_profit = price - min_price
                
        return max_profit