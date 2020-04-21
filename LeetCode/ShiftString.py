"""
1. loop over the shifts for each shift
2.    define direction = shift[0] and amount = shift[1]
3.    check if direction is 0 so do left shift using s[amount:] + s[:amount]
4.    otherwise direction is 1 do the right shift using s[-amount:] + s[:-amount]
5. return our final s
"""

class Solution:
    def stringShift(self, s, shift):
        for val in shift:
            d, amnt = val[0], val[1]
            if d == 0:
                # right shifr
                s = s[amnt:] + s[:amnt]
            elif d == 1:
                # left shift
                s = s[-amnt:] + s[:-amnt]
        return s



if __name__ == "__main__":
    sol = Solution()
    print(sol.stringShift("abc", [[0,1],[1,2]]))
    print(sol.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))