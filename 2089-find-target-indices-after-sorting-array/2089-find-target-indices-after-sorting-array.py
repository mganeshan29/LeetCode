class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        s=[]
        for i in range(len(nums)):
            if nums[i]==target:
                s.append(i)
        return s
