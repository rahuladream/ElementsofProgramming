"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

EXAMPLE
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
"""

class Solution:
    def countElements(self, arr):
        count = 0
        arry = lambda x: x + 1
        for val in arr:
            if arry(val) in arr:
                count = count + 1
        return count
        

if __name__ == "__main__":
    a = Solution()
    print(a.countElements([1,3,2,3,5,0]))
        