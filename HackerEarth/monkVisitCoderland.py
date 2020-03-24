"""
0 - start
N - 1 = end
T - input cases
N - checkpoint
C[i], L[i] - checkpoint to reach, Ltr of petro require
"""

cases = int(input())

for i in range(cases):
    n = int(input())
    c = list(map(int, input().split()))
    l = list(map(int, input().split()))
    cost = 0
    min = c[0]
    for j in range(0,n):
        if min <= c[j]:
            cost += min * l[j]
        else:
            min = c[j]
            cost += min * l[j]
    print(cost)