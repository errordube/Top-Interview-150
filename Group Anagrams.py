class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            anagram_map[sorted_word].append(i)
        return list(anagram_map.values())
