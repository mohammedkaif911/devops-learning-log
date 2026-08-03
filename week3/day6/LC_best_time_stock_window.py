class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy Day pointer
        max_profit = 0
        
        for right in range(1, len(prices)): # Sell Day pointer
            # If the transaction is profitable:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # We found a cheaper buy-day! Slide the window forward.
                left = right
                
        return max_profit