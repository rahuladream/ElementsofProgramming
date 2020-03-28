"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

INPUT:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

OUTPUT
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

N = int(input())
Data = []
for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'insert':
        Data.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(Data)
    elif cmd[0] == 'remove':
        Data.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        Data.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        Data.sort()
    elif cmd[0] == 'pop':
        Data.pop()
    elif cmd[0] == 'reverse':
        Data.reverse()
