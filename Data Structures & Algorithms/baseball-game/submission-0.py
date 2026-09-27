class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for num in operations:
            if num == "+":
                temp = int(stack[-1]) + int(stack[-2])
                stack.append(temp)
            elif num == "D":
                temp = int(stack[-1]) * 2
                stack.append(temp)
            elif num == "C":
                stack.pop()
            else:
                stack.append(int(num))
        return sum(stack)