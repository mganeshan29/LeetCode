class Solution:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        l=[]
        for i in s:
            if i.upper() in s and i.lower() in s:
                l.append(i)
        if l:
            l.sort()
            return l[-1].upper()
        else:
            return ""