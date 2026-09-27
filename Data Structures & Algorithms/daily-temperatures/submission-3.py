class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [30, 38, 30, 36, 35, 40, 28]
                                 p                        p
        res = [1, 4, 1, 2, 1, _, _]
        stack = [ (40, 5)]
        '''

        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            if not stack or n < stack[-1][0]:
                stack.append((n, i))
                continue
            while stack and n > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((n, i))
        
        while stack:
            res[stack[-1][1]] = 0
            stack.pop()
        return res
            
