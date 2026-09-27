class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        have 2 pointers one at the beginning and the end
        [1, 7, 2, 5, 4, 7, 3, 6]
            l  r

         calculate the area which would be the min of the value
         at l and r

         multiplied by r - l and then update the pointers by moving
         the one that has a less amount of capacity
        '''

        l, r = 0, len(heights) - 1
        max_area = 0
        temp = 0
        while l < r:
            temp = (r - l) * min(heights[l], heights[r])
            max_area = max(temp, max_area)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return max_area