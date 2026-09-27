class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        [1, 7, 2, 5, 4, 7, 3, 6]
            lr

         move the one that is less

         calculate the container area



        '''

        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            area = max(length * height, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area 
    