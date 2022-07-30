class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        sub = {}
        for s in words2:
            temp = {}
            for ch in s:
                if ch not in temp:
                    temp[ch]=1
                else:
                    temp[ch]+=1
            for key in temp:
                if key not in sub:
                    sub[key] = temp[key]
                elif temp[key] > sub[key]:
                    sub[key] = temp[key]
        for word in words1:
            pat = collections.Counter(word)
            flag = 1
            for key in sub:
                if pat[key] < sub[key]:
                    flag = 0
                    break
            if flag==1:
                res.append(word)
        return res