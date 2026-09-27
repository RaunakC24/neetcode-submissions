class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        use a set to keep track of each number
        add the number
        check if the number - 1 exists because that means 
        that the number is not the start of the sequence

        check if the number + 1 is in the sequence 

        [2, 20, 4, 10, 3, 4, 5]
         ^
        set = (2)
        check if 2 - 1 = 1 is in the set
        check if 2 + 1 = 3 is in the set
        
        max_count = 1

        set = (2, 20)
        max_count = 1

        set(2, 20, 4)
        max_count = 1

        set(2, 20, 4, 10)
        max_count = 1

        set(2, 20, 4, 10, 3)
        3 - 1 = 2 is in set
        max_count += 1 = 2
        3 + 1 = 4 is in set
        max_count += 1 = 3

        set(2, 20, 4, 10, 3)
        skip 4 because it is already in the set

        set(@, 20, 4, 10, 3, 5)
        5 - 1 = 4 max_count = 4
        5 + 1 = 6 max_count = 6

        nums=[0, 3, 2, 5, 4, 6, 1, 1]


        '''
        if not nums:
            return 0
        track = set(nums)
        max_seq = 1
        for n in nums:
            temp = 1
            if n - 1 not in track:
                while n + 1 in track:
                    temp += 1
                    n += 1
            max_seq = max(temp, max_seq)
        return max_seq





