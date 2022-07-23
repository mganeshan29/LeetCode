class Solution:
    def countAsterisks(self, s: str) -> int:
        flag=0
        c=0
        for i in s:
            if i =="|" :
                flag=not flag
            if flag==0:
                if i=="*":
                    c+=1
        return c
                
        
        
        
        
        
        
        
        
        
        
        
