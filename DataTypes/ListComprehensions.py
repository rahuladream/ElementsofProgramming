"""
INPUT:
X,Y,Z and N each of four seprate lines, respectively
1 -X
1 -Y
1 -Z
2 -N
OUTPUT
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

def list_comprehensions(x,y,z,n):
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (( i+j+k ) != n )]
    return result


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = list_comprehensions(x, y, z, n)
    print(output)