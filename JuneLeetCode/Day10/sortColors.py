class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.sortColors([2,0,2,1,1,0]))