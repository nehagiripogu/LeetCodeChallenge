class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key, value in freq.items():

            if value == 1:
                res.append(key)
        return res