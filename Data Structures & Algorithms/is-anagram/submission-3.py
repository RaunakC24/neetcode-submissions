class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        shashmap = Counter(s)
        thashmap = Counter(t)

        return shashmap == thashmap