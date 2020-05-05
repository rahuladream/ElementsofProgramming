class Solution:
    def findComplement(self, num):
        res = str(bin(num))[2:]
        return int("".join('1' if x == '0' else '0' for x in res), 2)


if __name__ == "__main__":
    a = Solution()
    print(a.findComplement(10))
        