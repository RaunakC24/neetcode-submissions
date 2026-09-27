class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for c in tokens:
            if c == "-" or c == "+" or c == "*" or c == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if c == "-":
                    stack.append(num2 - num1)
                elif c == "+":
                    stack.append(num2 + num1)
                elif c == "*":
                    stack.append(num2 * num1)
                elif c == "/":
                    print(num2 / num1)
                    print(int(num2/num1))
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(c))
        return stack[0]

        '''
        10, 0
        '''