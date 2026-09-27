class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for w in strs:
            temp = Counter(w)
            t = tuple(sorted(temp.items()))
            hashmap[t].append(w)
        
        return list(hashmap.values())
                