class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [1, 2, 3, 4]
        use a hashmap

        hashmap = {1: 1, }

        '''

        hashmap = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in hashmap:
                hashmap[numbers[i]] = i + 1
            else:
                return [hashmap[target - numbers[i]], i + 1]