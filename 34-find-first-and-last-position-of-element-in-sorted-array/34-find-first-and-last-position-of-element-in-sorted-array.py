class Solution:
    def searchRange(self, nums: List[int], k: int) -> List[int]:
        a=nums[::-1]
        if k not in nums:
            return [-1,-1]
        else:
            f=nums.index(k)
            l=a.index(k)
            return [f,len(nums)-l-1]
    