class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            word_len = len(word)
            res += str(word_len) + "|" + word
        return res

    def decode(self, s: str) -> List[str]:
        """go through the string
        check th efirst character and that means how many chars to read
        and then it it will check the enxt character 
        
        5|Hello5|World
                      s
        """
        res = []
        size = 0
        while size < len(s):
            num = ""
            while s[size].isnumeric():
                num += s[size]
                size += 1
            count = int(num)
            i = 0
            string= ""
            size += 1
            while i < count:
                string += s[size + i ]
                i += 1
            size += i
            res.append(string)
        return res
