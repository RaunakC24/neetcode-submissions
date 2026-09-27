class Solution:
    def isValid(self, s: str) -> bool:
        '''
        make a hashmap with the key being the closing and the value being the start

        if it is the starting one then add to the stack
        if it is a closing one then check fi the item at the top of the stack
        is the same as the closing one's value

        if there are items in the stack when done, then it means that it wasn't valid\

        ([{}])

        

        '''

        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack and stack[-1] != hashmap[c]:
                    return False
                stack.pop()
        if stack:
            return False
        return True
            