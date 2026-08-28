class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, line, length = [], [], 0

        for w in words:
            
            if length + len(w) + len(line) > maxWidth:
                res.append(self.justify(line, length, maxWidth))
                line, length = [], 0
            line.append(w)
            length += len(w)

        
        res.append(' '.join(line).ljust(maxWidth))
        return res

    def justify(self, line: list[str], length: int, maxWidth: int) -> str:
        gaps = len(line) - 1
        if gaps == 0:
            return line[0].ljust(maxWidth)

        spaces, extra = divmod(maxWidth - length, gaps)
        out = []
        for i, w in enumerate(line[:-1]):
            out.append(w)
            out.append(' ' * (spaces + (1 if i < extra else 0)))
        out.append(line[-1])
        return ''.join(out)
