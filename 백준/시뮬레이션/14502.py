from collections import deque
import sys
import copy

input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def back(x):
    if x == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                back(x+1)
                board[i][j] = 0

answer = 0

def bfs():
    global answer

    q = deque()
    arr = copy.deepcopy(board)
    visit = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i,j))
                visit[i][j] = True
    
    dx,dy = [1,0,-1,0],[0,1,0,-1]

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1: continue
            if visit[nx][ny]: continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx,ny))
                visit[nx][ny] = True
        
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1

    answer = max(answer, cnt)


back(0)
print(answer)