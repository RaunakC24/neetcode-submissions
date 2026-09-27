class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        have a hashmap to keep track of words
        and sort them by letters for as the key by making it a tuple
        hashmap = {"('a', 'r', 't')": ["tar"]}
        '''
        hashmap = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            hashmap[tuple(sorted(word))].append(word)
        return list(hashmap.values())




