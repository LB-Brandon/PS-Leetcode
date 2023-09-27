class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def sol1():
            min_price = float('inf')
            profit = float('-inf')
            for i in range(len(prices)):
                min_price = min(min_price, prices[i])
                profit = max(profit, prices[i] - min_price)
            return profit

        def sol2():
            min_price = sys.maxsize
            profit = 0
            for price in prices:
                min_price = min(min_price, price)
                profit = max(profit, price - min_price)
            return profit

        
        return sol2()