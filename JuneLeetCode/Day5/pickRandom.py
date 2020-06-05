import random, bisect
class Solution:
    
    def __init__(self, w):
        self.s = sum(w)
        # Weight of the arrau
        self.p = [-1] * len(w)
        for i in range(len(w)):
            w[i] += 0 if i == 0 else w[i-1]
            # sume of the cumlate weight of array
            self.p[i] = w[i] / self.s
            # sume of probability of with of the array

    def pickIndex(self):
        z = random.rand()
        # Random number is generated
        i = bisect.bisect_left(self.p, z)
        # if z in probability then it return index,
        # if z is not probability then the function bisect.bisect_left
        # searches for appropriate position of z where it can be inserted
        # It will return that index, if insertion is happened.
        return i
        



if __name__ == "__main__":
    a = Solution()
    print(a.pickIndex())
