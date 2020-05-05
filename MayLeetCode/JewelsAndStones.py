class Solution:
    def numJewelsInStones(self, J, S):
        myJ = set(J)
        count = 0
        for stone in S:
            if stone in myJ:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numJewelsInStones("aA", "aAAbbbb"))
    print(s.numJewelsInStones("z", "ZZ"))
    print(s.numJewelsInStones("ebd", "bbb"))