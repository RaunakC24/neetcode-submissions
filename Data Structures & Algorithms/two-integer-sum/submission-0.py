from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        create a hashmap
        at a number store the index as the value and the number is the key

        '''
        hashmap = {}
        for i, num in enumerate(nums): 
            if target - num not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[target - num], i]