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


- reduce()
reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to on values.
lets say have a list [1,2,3] and you have to find sum.
reduce(lambda x,y: x+y, [1,2,3])

- Fraction()
fraction() always return fraction part of the numerator & denominator
from fractions import Fraction as F
F(10,20)
return 
(1,2)


- to convert in binary number
bin(number), oct(number), hex(number)


- to a to z character remember
a is 97 in 123 is the end



Binary search is best when searching is middle or first or last
