class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        increasing order

        [1, 2, 3, 4] target = 3
         c
        hashmap = {}
        

        '''
        hashmap = {}
        for i, n in enumerate(numbers):
            if target - n not in hashmap:
                hashmap[n] = i
            else:
                return [hashmap[target - n]+1, i+1]



