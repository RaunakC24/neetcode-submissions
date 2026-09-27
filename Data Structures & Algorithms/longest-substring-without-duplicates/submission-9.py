class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        "zxyzxyz"
          l
             r 

        "xxxx"
          l  
            r  
        "pwwkew"
         l
           r
        set()
        '''

        l = 0
        max_length = 0
        contains = set()

        for r in range(len(s)):
            
            while s[r] in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length


