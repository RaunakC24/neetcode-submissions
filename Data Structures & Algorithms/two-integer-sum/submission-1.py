class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        use a hashmap to keep track of if target - current num is 
        in the hashmap and if it is then you ahve the answer
        '''

        hashmap = {}
        for i, n in enumerate(nums):
            if target - n not in hashmap:
                hashmap[n] = i
            else:
                return [hashmap[target - n], i]