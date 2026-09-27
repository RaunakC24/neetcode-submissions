class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        iterate through whole array
        add temperature to stack
        add smaller values to stack 

        '''
        '''
        brute force solution (0 n^2)
        '''
        result = [0] * len(temperatures) 
        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i 
                    break
        return result