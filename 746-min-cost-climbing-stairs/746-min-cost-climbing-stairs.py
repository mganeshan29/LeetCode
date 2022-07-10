class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x=0
        y=cost[0]
        for i in range(1,len(cost)):
            x,y=y,min(x+cost[i],y+cost[i])
        return min(x,y)