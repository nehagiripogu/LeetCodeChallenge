class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left = 0
        product = 1
        count = 0
        for right in range(len(nums)):

            product *= nums[right]

            # Shrink window if product >= k
            while product >= k:
                product //= nums[left]
                left += 1

            # Count valid subarrays
            count += (right - left + 1)

        return count