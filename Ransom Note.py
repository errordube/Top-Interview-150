class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = [0] * 26
        for ch in magazine:
            counts[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            i = ord(ch) - ord('a')
            counts[i] -= 1
            if counts[i] < 0:
                return False

        return True

        
