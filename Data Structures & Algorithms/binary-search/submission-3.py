class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [-1, 0, 2, 4, 6, 8]

          l         p    r

        l = 0
        r = len(nums)
        mid = l + r // 2
        check if nums at mid is the number
        if not then see if it less than the number
        if so move to left half
        otherwise move to the right half

        [-1, 0, 3, 5, 9, 12]
                   p
        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1