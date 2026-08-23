class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            if nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
