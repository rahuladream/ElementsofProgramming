"""
n versions [1, 2, 3, 4, 5 ..., n] and you want to find out the first bad one
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n

        while l <= h:
            mid = ( l + h) // 2

            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid):
                l = mid + 1
            else:
                h = mid - 1
        return -1
