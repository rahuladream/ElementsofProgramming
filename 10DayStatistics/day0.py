N = int(input())
X = input().split()

i = 0
summ = 0

for i in range (0, N):
    X[i] = int(X[i])
    summ += X[i]
mean = summ / N

X.sort()

if N % 2 == 0:
    median = (X[N//2] + X[N//2 - 1])/2
else:
    median = X[(N+1)/2]

counter = 0
index = 0
for i in range (0, N):
    if X.count(X[i]) > counter:
        counter = X.count(X[i])
        index = i
mode = X[index]
round(mean, 1)
round(median, 1)
print ( mean )
print ( median )
print ( mode )