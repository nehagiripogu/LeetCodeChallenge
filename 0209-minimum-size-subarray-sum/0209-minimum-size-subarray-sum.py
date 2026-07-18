class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minlen=float('inf')
        summ=0
        for right in range(len(nums)):
            summ+=nums[right]
            while summ>=target:
                minlen=min(minlen,right-left+1)
                summ-=nums[left]
                left+=1
        return 0 if minlen==float('inf') else minlen