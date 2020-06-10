class Solution:
    def searchInsert(self, nums, target):
        # classic binary search problem
        b, e = 0, len(nums)
        # beginning and end 0, length of nums
        while b < e:
            m = (b + e)//2
            # mid array to search and insert
            if nums[m] >= target:
                e = m
            # if not found insert and return index
            else:
                b = m + 1
            # if found return the index
        return b        


if __name__ == "__main__":
    a = Solution()
    print(a.searchInsert([1,3,5,6], 2))
