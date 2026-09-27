class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}
        stack = []
        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                first_num = stack.pop()
                second_num = stack.pop()
                if char == '+':
                    stack.append(first_num + second_num)
                elif char == '-':
                    stack.append(second_num - first_num)
                elif char == '*':
                    stack.append(first_num * second_num)
                elif char == '/':
                    stack.append(int(second_num / first_num))
        return stack[-1]