class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for i in nums:
            check.add(i)

        return len(check) != len(nums)