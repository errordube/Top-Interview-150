class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k, n = len(words[0]), len(words)
        total = k * n
        if len(s) < total:
            return []

        need = Counter(words)
        res = []

        for offset in range(k):
            window = Counter()
            count = 0
            left = offset
            for right in range(offset, len(s) - k + 1, k):
                word = s[right:right + k]
                if word not in need:
                    window.clear()
                    count = 0
                    left = right + k
                    continue

                window[word] += 1
                count += 1

                while window[word] > need[word]:
                    drop = s[left:left + k]
                    window[drop] -= 1
                    left += k
                    count -= 1

                if count == n:
                    res.append(left)
                    drop = s[left:left + k]
                    window[drop] -= 1
                    left += k
                    count -= 1

        return res
        
