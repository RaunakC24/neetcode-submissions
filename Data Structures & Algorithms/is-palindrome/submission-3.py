class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        create a new string that contains alphanumeric characters

        new_string = "wasitacaroracatisaw"

        then use two pointers one at the beginning and one at the end

        and check if they are both equal 
        ''' 
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        l, r = 0, len(new_string) - 1

        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1   

        return True   