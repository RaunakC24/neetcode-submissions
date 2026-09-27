class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1

        while l <= h:
            mid = (l + h) // 2
            if target < matrix[mid][0]:
                h = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else: 
                break
        # if l > h:
        #     return False
        l, h = 0, len(matrix[0]) - 1
        while l <= h:
            m = (l + h) // 2
            if target < matrix[mid][m]:
                h = m - 1
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                return True
        return False


                # left, right = 0, len(matrix[0]) - 1
                # while left <= right:
                #     m = (left + right) // 2
                #     if matrix[mid][m] > target:
                #         high = m - 1
                #     elif matrix[mid][m] < target:
                #         left = m + 1
                #     else:
                #         return True
        return False
