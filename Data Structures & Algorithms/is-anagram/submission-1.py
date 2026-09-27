from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_word = defaultdict(int)
        t_word = defaultdict(int)

        for a, b in zip(s, t):
            s_word[a] += 1
            t_word[b] += 1
        
        return s_word == t_word
        æ