class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        return len(nums)-(reduce(xor, nums, 0)==0) if any(nums) else 0