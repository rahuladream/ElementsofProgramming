import math
class Solution:
    def isPowerOfTwo(self, n):
        
        if n < 0 or n == 0:
            # return if value is 0 
            return False
        
        # function of check log base 2 i.e if the power of 2
        return (math.ceil(math.log10(abs(n)) / math.log10(2)) == math.floor((math.log10(abs(n)) / math.log10(2))))



if __name__ == "__main__":
    a = Solution()
    print(a.isPowerOfTwo(-16))        