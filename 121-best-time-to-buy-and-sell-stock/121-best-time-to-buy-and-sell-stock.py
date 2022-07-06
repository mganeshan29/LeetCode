class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minsofar=prices[0]
        for i in range(0,len(prices)):
            minsofar=min(minsofar,prices[i])
            profit=prices[i]-minsofar
            maxprofit=max(maxprofit,profit)
        return maxprofit
            #time:O(n) space o(1):constant
