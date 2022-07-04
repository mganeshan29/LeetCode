class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_for_all=nums[0]
        # curr_max=nums[0]
        # for i in range(1,len(nums)):
        #     curr_max=max(nums[i],curr_max+nums[i])
        #     max_for_all=max(max_for_all,curr_max)
        # return max_for_all
        maxforall=nums[0]
        currmax=nums[0]
        for i in range(1,len(nums)):
            currmax=max(nums[i],currmax+nums[i])
            maxforall=max(maxforall,currmax)
        return maxforall
            