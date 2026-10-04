class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map={}
        for word in strs:
            sortedword="".join(sorted(word))
            if sortedword in anagrams_map:
                anagrams_map[sortedword].append(word)
            else:
                anagrams_map[sortedword] = [word]
        return list(anagrams_map.values())
        
        