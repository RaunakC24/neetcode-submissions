class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        l, r = 0, len(res) - 1
        while l < r:
            if not res[l].isalnum():
                l += 1
            if not res[r].isalnum():
                r -= 1
            
            if res[l].lower() != res[r].lower():
                print(s[l])
                print(s[r])
                return False
            
            l += 1
            r -= 1
        
        return True