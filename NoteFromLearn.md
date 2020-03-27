## LEARNING FROM THE CODING SESSION

to take any input in python

- storing into the format of list
arr = list(map(int, input().split()))

- storing into the format of set
superSet = set(map(int, input().split()))

- taking multiple input i.e. n
for i in range(n):
B = list(map(int, input().split()))

- if want to change -ve to +ve in any case
use abs(value)

- to check the supper subset in case of ste
A.issuperset(B)

- to find second largest number
sort the list or array
arr.sort()
arr[-2]

- to take like multiple inputs from the use

students = [[input(), float(input())] for i in range(int(input())]
(it will take input individually) 
Harry
37.21 like this
this will print([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]])