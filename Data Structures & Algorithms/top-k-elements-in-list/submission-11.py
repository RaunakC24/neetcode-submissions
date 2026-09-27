import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [1, 2, 2, 3, 3, 3], k = 2

        use counter to create a hashmap
        {1: 1, 2: 2, 3: 3}

        create a min heap of size 2
        we would need to switch the order of the paits to be count, number

        keep adding to the minheap until the size is 2
        then we would compare 3 with the smallest value in the min heap 
        3 is bigger than 1 then we would remove 1 from the minheap and add 3 to it

        then we can just pop the remaining values and add the number to a list
        '''
        heap = []
        hashmap = Counter(nums)
        hashmap_list = list(hashmap.items())
        ans = []
        size = 0
        i = 0
        



        for num, occ in hashmap_list:
            if size < k: 
                heapq.heappush(heap, (occ, num))
                size += 1
                
            elif heap[0][0] < occ:
                heapq.heappop(heap)
                heapq.heappush(heap, (occ, num))
        for occ, num in heap:
            ans.append(num)
        return ans

