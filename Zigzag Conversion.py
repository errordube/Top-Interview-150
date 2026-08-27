class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        cur, dir = 0, -1
        for c in s:
            rows[cur].append(c)
            if cur == 0 or cur == numRows - 1:
                dir = -dir
            cur += dir
        return "".join("".join(r) for r in rows)
        
