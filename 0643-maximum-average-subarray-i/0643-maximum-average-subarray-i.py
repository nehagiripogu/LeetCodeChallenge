class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=sum(nums[:k])
        maxsum=windowsum/k
        for i in range(k,len(nums)):
            windowsum-=nums[i-k]
            windowsum+=nums[i]
            maxsum=max(maxsum,windowsum/k)
        return maxsum