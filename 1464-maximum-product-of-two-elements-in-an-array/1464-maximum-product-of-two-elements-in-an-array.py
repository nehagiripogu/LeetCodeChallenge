class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            res.append(nums[i]-1)
        res.sort()
        ans=res[-1]*res[-2]
        return ans