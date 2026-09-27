class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [10, 1, 5, 6, 7, 1]
             l  r

         move left pointer once a lower number is found
         check if number at the right pointer is less than the 
         left pointer and if so move left to right

         otherwise calculate the max_profit and update it 
         


        '''

        l = 0
        profit = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
        return profit