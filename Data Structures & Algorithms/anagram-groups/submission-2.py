class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        solution 1:
        ["act","pots","tops","cat","stop","hat"]
        hashmap that keeps track of every letter in a word
        hashmap = {a: 1, c: 1, t: 1}
        
        second hashmap that uses that uses the previous hashmap as the key and an array as the value

        2ndhashmap = {}

        solution 2: 
        for every word just call sort and check if the word is in the hashmap. if it is just append to the list which is the value at a key. if it isn't in the hasmap then add the sorted word as a key and then add the original word to the list for that key.

        solution 3:
        create a list of length of 26 and loop through every letter. add the "letter" to the list  by doing ord(char) - ord('a'), this will give it's ascii value from 0-25 in the array.

         then the key of the hashmap is the 26 lnegth array and the value is a list of the word. at the end call the .values() to get the resulting list
        '''
        hashmap = defaultdict(List)
        for word in strs:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            t_arr = tuple(arr)
            if t_arr not in hashmap:
                hashmap[t_arr] = [word]
            else:
                hashmap[t_arr].append(word)
        return list(hashmap.values())
            
        