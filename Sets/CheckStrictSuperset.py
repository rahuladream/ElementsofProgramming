"""
INPUT:
A and n other sets
Your job is to find whether set A is a strict superset of each of the N sets.

True if A is strict superset of the N sets. Otherwise print False.

A strict superset has atleast one element does not exist in its subset.

Example
Set([1, 3, 4]) is strict superset of Set([1, 3])
Set([1, 3, 4]) is not strict superset of Set([1, 3, 4])

fuck multirange input
"""

A = set(map(int, input().split()))
n = int(input())
setSet = True
for i in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        setSet = False
        break
print(setSet)