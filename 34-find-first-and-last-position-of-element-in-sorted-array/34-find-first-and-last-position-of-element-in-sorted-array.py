class Solution:
    def searchRange(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        first=last=-1
        l=0
        h=len(nums)-1
        while(l<=h):
            m=(l+h)//2
            if nums[m]>k:
                h=m-1
            elif nums[m]<k:
                l=m+1
            else:
                first=m
                h=m-1
        l=0
        h=len(nums)-1
        while(l<=h):
            m=(l+h)//2
            if nums[m]>k:
                h=m-1
            elif nums[m]<k:
                l=m+1
            else:
                last=m
                l=m+1
        return [first,last]