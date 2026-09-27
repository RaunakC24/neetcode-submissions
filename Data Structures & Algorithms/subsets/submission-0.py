class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total_sub, temp = [], []

        def helper(i, nums, total_sub, temp):
            if i >= len(nums):
                total_sub.append(temp.copy())
                return

            temp.append(nums[i])
            helper(i + 1, nums, total_sub, temp)
            temp.pop()

            helper(i + 1, nums, total_sub, temp)
        helper(0, nums, total_sub, temp)
        return total_sub