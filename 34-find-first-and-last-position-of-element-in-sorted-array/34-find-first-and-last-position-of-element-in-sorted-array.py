class Solution:
    def searchRange(self, nums: List[int], k: int) -> List[int]:
        # a=nums[::-1]
        # if k not in nums:
        # if len(nums)==0:
        #     return [-1,-1]
        # else:
        #     f=nums.index(k)
        #     l=a.index(k)
        #     return [f,len(nums)-l-1]
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