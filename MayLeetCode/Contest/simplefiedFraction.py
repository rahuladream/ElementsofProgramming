from fractions import Fraction
class Solution:
    def simplifiedFractions(self, n):
        res = []
        deno = [c for c in range(2, n)]
        nemo = [n for n in range(1, n)]
        if n == 1:
            return []
        else:
            for c in deno:
                
        return res




if __name__ == "__main__":
    a = Solution()
    print(a.simplifiedFractions(2))