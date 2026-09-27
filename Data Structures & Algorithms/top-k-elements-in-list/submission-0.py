class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
         
        create a hashmap that stores the count 
        then use a max heap to store the highest counts 

        then use a whlie loop that adds the numbers to the result array
        '''

        count = Counter(nums)
        
        maxHeap = []
        res = []
        for i, n in enumerate(count):
            heapq.heappush(maxHeap, (-count[n], n))
        count = 0
        while count < k:
            res.append(heapq.heappop(maxHeap)[1])
            count += 1
        return res

        
        
        
