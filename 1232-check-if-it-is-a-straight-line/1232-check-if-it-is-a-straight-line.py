class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)-1
        for i in range(1, n):
            if(
                (coordinates[i][0] - coordinates[i-1][0])
              * (coordinates[i+1][1] - coordinates[i][1])
               != 
                (coordinates[i][1] - coordinates[i-1][1]) 
              * (coordinates[i+1][0] - coordinates[i][0])
              ):
                return False
        return True
            
            