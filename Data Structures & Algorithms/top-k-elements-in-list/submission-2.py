import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        use a max heap to keep the most frequent one at the top
        but uses a hashmap to keep track of the frequency
            p
        [1, 2, 2, 3, 3, 3]
        add one to the hashamp {"1": 1}
        then add the frequency to the value in the heap
        '''
        hashmap = Counter(nums)
        heap = []
        res = []
        i = 0

        for num, freq in hashmap.items():
            heapq.heappush(heap, (-freq, num))

        while i < k:
            freq, num = heapq.heappop(heap)
            res.append(num)
            i += 1
        return res