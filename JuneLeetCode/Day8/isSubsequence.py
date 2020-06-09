class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0: return True
        if len(t) == 0: return False
        i, j = 0, 0
        while j < len(s) and i<len(t):
            if s[j] == t[i]:
                j = j + 1
            i = i + 1
        return j == len(s)


if __name__ == "__main__":
    a = Solution()
    print(a.isSubsequence("axc","ahbgdc"))