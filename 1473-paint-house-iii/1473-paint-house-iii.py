class Solution:
    def minCost(self, houses, cost, m, n, target) -> int:
        
        @functools.lru_cache(None)
        def foo(i,t,p):
            if t<0:
                return float('inf')
            if i==len(houses):
                return 0 if t==0 else float('inf')
            
            temp=float('inf')

            # if already painted 
            if houses[i]:
                # if previous color matches with current do not decrease
                # the target value else decrease
                if houses[i]==p:    val=foo(i+1, t, houses[i])
                else:               val=foo(i+1, t-1, houses[i])
                temp=min(val, temp)
                
            # if not painted
            else:
                # try out all colors and return the min
                for color in range(1,n+1):
                    # if previous color matches with current do not decrease
                    # the target value else decrease
                    if color==p:    val=foo(i+1, t, color)+cost[i][color-1]
                    else:           val=foo(i+1, t-1, color)+cost[i][color-1]
                    temp=min(val, temp)
            
            return temp
                
        res=foo(0, target, 0)
        return res if res<float('inf') else -1