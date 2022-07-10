class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minn = 10e5 #inittial min (max value)
        result = -1
        for index,point in enumerate(points):    # enumerate(points) gives (i,pints[i])
            if x == point[0] or y ==point[1]:       #valid point condition check
                man_distance=abs(point[0]-x)+abs(point[1]-y)    #manhattan distance for valid points
                if minn > man_distance:      #compare distance
                    minn = man_distance
                    result = index
        return result
                