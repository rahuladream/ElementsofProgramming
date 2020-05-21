

num = int(input())

for i in range(num):
    s1 = input()
    s2 = input()
    
    if tuple(s1) in tuple(s2):
        print(True)
    else:
        print(False)