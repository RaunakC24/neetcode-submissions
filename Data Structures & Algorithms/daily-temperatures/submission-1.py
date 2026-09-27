class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
    res=[1, 4, 1, 2, 1, 0, 0]
        [30, 38, 30, 36, 35, 40, 28]
                                  i
        stack = [(40, 5)] 

    res=[1, 4, 1, 2, 1, 0, 0]
        [30, 38, 30, 36, 35, 40, 28]
                                  i
        stack = [(40, 5), (28, 6)]
        store index at where temperature is at
        '''

        res = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop() 
            stack.append((n, i))
            if not stack or n < stack[-1][0]:
                stack.append((n, i))
        
        while stack:
            temp, place = stack.pop()
            res[place] = 0
        return res