"""
Count the number of islands

Input:
11110
11010
11000
00000

Output: 1

"""

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        # import pdb; pdb.set_trace()
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)