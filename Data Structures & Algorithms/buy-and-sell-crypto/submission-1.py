class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        go through the array and look for the price that has the lowest price
        change the start of the window when a number is less
        if the number is greater than the prev then just see if the max_profit needs to be increased
        '''

        max_profit = 0
        min_price = 101
        for price in prices:
            min_price = min(price, min_price)
            if min_price < price:
                max_profit = max(max_profit, price - min_price)
        return max_profit
