# inplace algorithm: 
"""
An in-place algorithm is an algorithm that does not need an extra space and produces
an output in the same memory that contains the data by transforming the input ‘in-place’.
However, a small constant extra space used for variables is allowed.
"""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        rev = n * [0]
        for i in range(0, n):
            rev[n - i - 1] = s[i]

        for i in range(0, n):
            s[i] = rev[i]


if __name__ == "__main__":
    a = Solution()
    print(a.reverseString(["H","a","n","n","a","h"]))