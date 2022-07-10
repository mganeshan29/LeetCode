class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        maxw=0
        for i in accounts:
            s=sum(i)
            maxw=max(maxw,s)
        return maxw