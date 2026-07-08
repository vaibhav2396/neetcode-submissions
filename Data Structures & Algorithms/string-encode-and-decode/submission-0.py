class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for st in strs:
            enc += str(len(st))
            enc += '#'
            enc += st
        return enc

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            temp = ""
            while s[i] != '#':
                temp += s[i]
                i += 1
            result.append(s[i+1: (i+1+int(temp))])
            i += 1+int(temp)
            
        return result
