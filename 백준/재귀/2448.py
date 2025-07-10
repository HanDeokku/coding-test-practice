import sys
input = sys.stdin.readline

n = int(input())

m = n * 2 - 1

picture = [[" "] * m for _ in range(n)]

def recursion(size, x, y):
    if size == 3:
        picture[x][y] = "*"
        picture[x+1][y-1] = picture[x+1][y+1] = "*"
        for i in (-2,-1,0,1,2):
            picture[x+2][y+i] = "*"
        return
    
    recursion(size//2, x, y)
    recursion(size//2, x+size//2, y-size//2)
    recursion(size//2, x+size//2, y+size//2)

recursion(n, 0, n-1)

for pic in picture:
    print("".join(pic))