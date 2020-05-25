a = int(input())
for i in range(a):
    i = (input())
    j = (input())
    setx = set([a for a in i])
    sety = set([y for y in j])
    if setx.intersection(sety) == set():
        print("NO")
    else:
        print("YES")