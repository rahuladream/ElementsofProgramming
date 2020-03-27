"""
INPUT:
n no. of items
A[] of n intergers separated by a space

OUTPUT
print runner up score
"""



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = max(arr)
    new_arr = []
    for i in range(len(arr)):
        if arr[i] < largest:
            new_arr.append(arr[i])
    print(max(new_arr))