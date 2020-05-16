import math
class Solution:
    def simplifiedFractions(self, n):
        res = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i < j and math.gcd(i, j) == 1:
                    res.append("{}/{}".format(i, j))
        return res



if __name__ == "__main__":
    a = Solution()
    print(a.simplifiedFractions(2))