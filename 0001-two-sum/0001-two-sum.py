class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq=set()
        for i,num in enumerate(nums):
            need=target-nums[i]
            if need in freq:
                sec=nums.index(need)
                return i, sec
            freq.add(nums[i])
        