from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)

        p = Counter(p)
        ans = []
        windos = None
        for i in range(0, n, m+1):
            if i == 0:
                windos = Counter(s[:m])
            else:
                windos[s[i-1]] -= 1
                windos[s[i+m-1]] += 1
            if len(windos - p) == 0:
                ans.append(i)
        return ans