"""
:type
Array
:output
Largest sum integer

INPUT:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

YOUR PATTERN SHOULD BE
a b c
  d
e f g
To find out the largest sum array

OUTPUT:
19
"""


# !/bin/python3

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_arr = []
    for i in range(4):
        for j in range(4):
            sum_arr.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]+ arr[i+2][j+2])
    print(max(sum_arr))

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
