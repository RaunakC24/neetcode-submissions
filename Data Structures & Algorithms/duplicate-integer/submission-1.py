class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        for n in nums:
            if n not in contains:
                contains.add(n)
            else:
                return True
        return False