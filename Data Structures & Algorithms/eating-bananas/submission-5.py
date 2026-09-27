class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [1, 2, 3, 4], h = 9
            ^
        
        iterate through the entire array
        
        [4, 10, 23, 25]\

        [3, 6, 7, 11]

        '''

        piles.sort()
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = (l + r) // 2

            count = 0
            for i in piles:
                count += math.ceil(i / mid)
            if count <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans