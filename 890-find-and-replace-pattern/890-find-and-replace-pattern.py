class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p=""
        res=[]
        for i in pattern:
            p+=str(pattern.index(i))
        for ele in words:
            temp=""
            for j in ele:
                temp+=str(ele.index(j))
            # res.append(temp)
            if temp==p:
                res.append(ele)
        return res