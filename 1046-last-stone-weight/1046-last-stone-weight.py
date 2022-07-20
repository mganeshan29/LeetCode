class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>=2:
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            stones.append(x-y)
        return stones[0]
        