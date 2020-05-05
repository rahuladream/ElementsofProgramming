import collections
class Solution:
    def firstUniqChar(self, s):
        if s:
            sorte_ = sorted(collections.Counter(s).items(), key=lambda x: x[1])[0]
            if sorte_[1] == 1:
                if sorte_[0] in s:
                    return s.index(sorte_[0])
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))