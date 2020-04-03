"""
create rangoli
"""
import string

def print_rangoli(size):
    start_range = 97
    end_range = 123
    looking_characters = chr(start_range+size)
    mid = size - 1
    for i in range(size-1, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[mid - j] = row[mid + j] = chr(start_range+j+i)
        print('-'.join(row))

    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(0, size - i):
            row[mid - j] = row[mid + j] = chr(start_range+j+i)
        print('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)