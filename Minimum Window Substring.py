class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        required = len(need)
        window = {}
        formed = 0
        left = 0
        best = (float('inf'), 0, 0)  

        for right, ch in enumerate(s):
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    formed += 1

            while formed == required:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)
                lc = s[left]
                if lc in need:
                    window[lc] -= 1
                    if window[lc] < need[lc]:
                        formed -= 1
                left += 1

        return "" if best[0] == float('inf') else s[best[1]:best[2] + 1]
        
