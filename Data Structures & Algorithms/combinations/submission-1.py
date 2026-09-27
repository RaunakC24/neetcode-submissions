class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        have a total combination array and a temp array

        [1, 2, 3]

        1 -> 2, 1 -> 3
        2 -> 3

        use a helper function
        '''
        totalComb, temp = [], []
        def helper(i, totalComb, temp, n, k):
            if len(temp) == k:
                totalComb.append(temp.copy())
                return
            if i > n:
                return
            
            for i in range(i, n + 1):
                temp.append(i)
                helper(i + 1, totalComb, temp, n, k)
                temp.pop()
        helper(1, totalComb, temp, n, k)
        return totalComb
