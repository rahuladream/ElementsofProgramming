"""
Find the judge in the town
"""


class Solution:
    def findJudge(self, N, trust):
        trusted = [0] * (N + 1)
        for (i, j) in trust:
            trusted[i] -= 1
            trusted[j] += 1

        for k in range(1, len(trusted)):
            if trusted[k] == N -1:
                return k
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))

        