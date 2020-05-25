import collections
class Solution:
    def frequencySort(self, s):
        tmp = ""
        freq = sorted(collections.Counter(s).items(), key=lambda x:x[1], reverse=True)
        for x in freq:
            tmp += x[0] * x[1]
        return tmp

if __name__ == "__main__":
    a = Solution()
    print(a.frequencySort("Aabb"))