"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above
for each from to. Each value should be space-padded to match the width of the binary value of .


"""
import math
def print_formatted(number):
    w = 0
    max_length = math.floor(math.log(n, 2)) + 1
    for i in range(1,number+1):
        w += 1
        print_value = "{} {} {} {}".format(str(i).rjust(max_length), str(oct(i))[2:].rjust(max_length), str(hex(i))[2:].upper().rjust(max_length), bin(i)[2:].rjust(max_length))
        print(print_value)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)