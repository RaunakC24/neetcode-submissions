class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [3,4,5,6] target = 7

        hashmap that tracks a number and its index

        we can check if the target - number exists in the hashmap which means we have a sum that we saw
        '''

        hashmap = {}
        for i, num in enumerate(nums):
            if target - num not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[target - num], i] 