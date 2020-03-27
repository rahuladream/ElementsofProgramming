"""
reduct(lambda x,y : x+y, [1,2,3])
6

reduce(lambda x,y : x+y, [1,2,3], -3)

from fractions import gcd
reduce(gcd, [2,4,8], 3)
1
"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    import pdb; pdb.set_trace()
    return t.numerator, t.denominator   

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

