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
        diff= []
        days = 0
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while(diff and temperatures[i] > diff[-1][1]):
	            days=i-diff[-1][0]
	            result[diff[-1][0]] = days
	            diff.pop()

            diff.append((i, temperatures[i]))

            if( not diff):
                diff.append((i, temperatures[i]))
        return result
        # res = [0] * len(temperatures)
        # stack = []
        # for i, n in enumerate(temperatures):
        #     while stack and n > stack[-1][0]:
        #         res[stack[-1][1]] = i - stack[-1][1]
        #         stack.pop() 
        #     stack.append((n, i))
        #     if not stack or n < stack[-1][0]:
        #         stack.append((n, i))
        
        # while stack:
        #     temp, place = stack.pop()
        #     res[place] = 0
        # return res