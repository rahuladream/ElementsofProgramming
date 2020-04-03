"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Please don't confuse sum
Keep in mind it's contiguous subarray
"""
import sys
class Solution:
    def maxSubArray(self, nums):
        arr_len = len(nums)
        max_sum = nums[0]
        max_sum_end = nums[0]

        for i in range(1, arr_len):
            max_sum = max(nums[i], max_sum + nums[i])
            max_sum_end = max(max_sum, max_sum_end)
        return max_sum_end


if __name__ == '__main__':
    a = Solution()
    print(a.maxSubArray([-2, -1]))
