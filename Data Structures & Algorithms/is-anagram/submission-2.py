class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        use a hashmap and then compare both of them
        '''
        first = Counter(s)
        second = Counter(t)

        return first == second