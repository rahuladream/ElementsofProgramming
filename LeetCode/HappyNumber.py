"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 
1. Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution:
    def isHappy(self, n):
        sum = 0
        
        for number in str(n).split()[0]:
            sum += int(number)*int(number)
        if 1<= sum and sum <=9:
            if sum == 1 or sum == 7:
                return True
            else:
                return False
        else:
            return self.isHappy(sum)
        
if __name__ == '__main__':
    b = Solution()
    b.isHappy(19)