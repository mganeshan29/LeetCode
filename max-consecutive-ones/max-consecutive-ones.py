class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        max_c=0
        for i in nums:
            c+=1
            if i!=1:
                c=0
            if c>max_c:
                max_c=c
        return max_c
                