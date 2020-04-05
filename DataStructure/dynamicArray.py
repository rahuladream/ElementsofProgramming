"""
:arg

initilize
lastAnswer = 0

Query 1 x y
seqList = (x ^ lastAnswer) % N)

Query 2 x y
seqList = (x ^ lastAnswer) % N)

"""

# !/bin/python3

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

lastAnswer = 0
S0 = []
S1 = []
seqList = 0
matrix = [[] for i in range(n)]

print(matrix)
for i in range(q):
    if queries[i][0] == 1:
        matrix[(queries[i][1] ^ lastAnswer) % n].append(queries[i][2])
    else:
        seqList = (queries[i][1] ^ lastAnswer) % n
        size = len(matrix[seqList])
        lastAnswer = matrix[seqList][queries[i][2] % size]
        print(lastAnswer)