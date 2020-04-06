"""
Given two positive integers M and N, after adding M and N if number of digits in M+N and N are same return N otherwise return M+N.

Input:
First line of input contains T denoting number of testcases. For each test case there will be two space seperated positive integers M and N.

Output:
If number of digits in M+N is same as N print N otherwise print M+N.

Constraints:
1 <= T <= 100
1 <= M <= 109
1 <= N <=109

Example:
Input:
2
44 22
99 12

Output:
22
111
"""


n = int(input())
digits = []
for _ in range(2):
    digits.append(list(map(int, input().split())))

for v in digits:
    csm = str(sum(v))
    if len(csm) == len(str(v[-1])):
        print(v[-1])
    else:
        print(csm)