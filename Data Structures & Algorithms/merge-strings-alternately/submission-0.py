class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = False
        if len(word1) > len(word2):
            res = False
        elif len(word2) > len(word1):
            res = True
        list1 = list(word1)
        list2 = list(word2)
        final_string = []

        for i in range(min(len(list1), len(list2))):
            final_string.append(list1[i])
            final_string.append(list2[i])
        print(i)
        print(len(list1))
        if i == len(list1)-1 and i == len(list2)-1:
            return ''.join(final_string)
        
        if res:
            for j in range(i+1, len(list2)):
                final_string.append(list2[j])
            return ''.join(final_string)
        else:
            for j in range(i+1, len(list1)):
                final_string.append(list1[j])
            return "".join(final_string)
        

