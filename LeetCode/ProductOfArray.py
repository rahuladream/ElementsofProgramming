"""

"""



class Solution:
    def productExceptSelf(self, nums):
        result = []
        for n in nums:
            result.append(result[-1] * n if result else n)
        backward = None
        i = len(nums) - 1
        while i >= 0:
            backward = backward * result[i+1] if backward != None else 1
            result[i] = result[i-1] * backward if i-1 >= 0 else backward
            i -= 1
        return result


if __name__ == "__main__":
    soln = Solution()
    print(soln.productExceptSelf([1,2,3,4]))