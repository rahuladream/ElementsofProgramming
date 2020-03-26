"""
We have seen that lists are mutable (they can be changed), and
tuples are immutable (they cannot be changed).

Change the character at a given index and then print

"""

"""
We have seen that lists are mutable (they can be changed), and
tuples are immutable (they cannot be changed).

Change the character at a given index and then print

"""

def mutate_string(s, i, c):
    s_new = s[:int(i)] + c + s[int(i+1):]
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)