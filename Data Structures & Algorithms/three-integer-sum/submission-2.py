class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort the array
        [-4, -1, -1, 0, 1, 2]

        create a res array

        pick a number so iterate through the array to pick the first number

        then have a hashmap to see if the target - selected number 
        - curr is in the hashmap


        = 0
        create res array
        sort array
        create a hashset that sorts the group of three numbers
        to make sure we don't get duplicates
        have a for loop for the whole array that stops 2 before the ned
        then create a hashset for if the 3sum is there
        

        '''

        res = []
        nums.sort()
        check = set()
        for i in range(len(nums) - 2):
            third_num = set()
            for j in range(i + 1, len(nums)):
                if 0 - nums[i] - nums[j] not in third_num:
                    third_num.add(nums[j])
                else:
                    three_nums = sorted((nums[i], nums[j], 0 - nums[i] - nums[j]))
                    t_nums = tuple(three_nums)
                    if t_nums not in check:
                        check.add(t_nums)
                        res.append([nums[i], nums[j], 0 - nums[i] - nums[j]])
        return res
                




