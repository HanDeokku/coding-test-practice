import sys
input = sys.stdin.readline
n = int(input())

board = [[0] * 101 for _ in range(101)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]


for _ in range(n):
    y, x, d, g = map(int, input().split())
    curve = [d]
    board[x][y] = 1

    for i in range(g):
        for j in range(len(curve)-1,-1,-1):
            curve.append((curve[j]+1)%4)
    
    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]
        board[x][y] = 1

answer = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
            answer += 1

print(answer)