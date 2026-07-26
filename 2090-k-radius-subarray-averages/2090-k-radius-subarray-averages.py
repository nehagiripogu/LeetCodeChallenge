class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        window_size = 2 * k + 1
        if window_size > n:
            return ans
        window_sum = sum(nums[:window_size])
        ans[k] = window_sum // window_size
        for i in range(window_size, n):
            window_sum += nums[i]                
            window_sum -= nums[i - window_size]    
            center = i - k
            ans[center] = window_sum // window_size
        return ans