class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1,2):
                s+=sum(arr[i:j])
        return s