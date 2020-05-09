

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num < 0):
            return False
        if (num == 0) or (num == 1):
            return True
        i = 1
        sum = 0
        while sum < num:
            sum += i
            if sum == num:
                return True
            i += 2
        return False
    

if __name__ == "__main__":
    a = Solution()
    print(a.isPerfectSquare(1))