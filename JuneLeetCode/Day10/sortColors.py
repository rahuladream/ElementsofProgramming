class Solution:
    def sortColors(self, nums):
        beg, mid, end = 0, 0, len(nums) - 1

        while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                mid += 1
                beg += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:
                mid += 1
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.sortColors([2,0,2,1,1,0]))