"""
Given an array of things group anagram together
"""
from itertools import groupby

class Solution:
    def groupAnagrams(self, strs):
        tmp = lambda strs: sorted(strs)
        res = [list(value) for key, value in groupby(sorted(strs, key = tmp), tmp)]
        return res


if __name__ == "__main__":
    in_ = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution()
    print(res.groupAnagrams(in_))
        