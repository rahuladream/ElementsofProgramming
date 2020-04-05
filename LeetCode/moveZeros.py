"""
Update all the non-zero with the original value
Remaining element update with zero
"""


class Solution:
    def moveZeroes(self, nums):
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.moveZeroes([0,1,0,3,12]))