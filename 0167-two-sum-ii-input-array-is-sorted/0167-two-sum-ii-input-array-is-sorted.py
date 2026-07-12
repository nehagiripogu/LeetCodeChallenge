class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in num_map:
                return [num_map[complement]+1,i+1]
            num_map[num]=i
        return None

        