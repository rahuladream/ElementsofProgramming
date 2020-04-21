"""
Collection of positive stones

if x == y :
    then destroy x and y return 0
elif x != y:
    new weight = y - x
return 0 if nothing left
"""


class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            if len(stones) == 0:
                return 0
            elif len(stones) == 1:
                return "".join(str(a) for a in stones)
            if stones[-1] == stones[-2]:
                stones.pop(-1)
                stones.pop(-1)                
            else:
               res = abs(stones[-1] - stones[-2]) 
               stones.pop(-1)
               stones[-1] = res
        
        if len(stones):
            return stones[-1]
        return 0


if __name__ == "__main__":
    x = Solution()
    print(x.lastStoneWeight([1,3]))