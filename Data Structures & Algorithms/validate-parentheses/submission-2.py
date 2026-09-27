class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            else:
                if not stack and c in hashmap.keys():
                    return False
                if stack:
                    top_element = stack.pop()
                    if top_element != hashmap[c]:
                        return False
        return True if not stack else False