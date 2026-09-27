class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word1 = {}
        word2 = {}
        for i in s:
            if i not in word1:
                word1[i] = 1
            else: 
                word1[i] += 1
        for i in t:
            if i not in word2:
                word2[i] = 1
            else: 
                word2[i] += 1
        print(word1)
        print(word2)
        if word1 != word2:
            return False
        else:
            return True