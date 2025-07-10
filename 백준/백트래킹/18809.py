from itertools import combinations
from collections import deque
import sys

imput = sys.stdin.readline

n, m, g, r = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(n)]

possible = []
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            possible.append((i,j))

dx, dy = [1,0,-1,0], [0,1,0,-1]

def bfs(result):
    visit_r = [[False] * m for _ in range(n)]
    visit_g = [[False] * m for _ in range(n)]
    time = [[0] * m for _ in range(n)]
    flower = [[False] * m for _ in range(n)]

    q = deque(result)
    for (i,j,c,t) in result:
        if c == 1:
            visit_r[i][j] = True
        else:
            visit_g[i][j] = True

    cnt = 0

    while q:
        x, y, color, t = q.popleft()
        if flower[x][y]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
            if garden[nx][ny] == 0: continue
            if flower[nx][ny]: continue
            if color == 1:
                if visit_r[nx][ny]: continue
                if visit_g[nx][ny]:
                    if time[nx][ny]-1 == t:
                        cnt += 1
                        flower[nx][ny] = True
                else:
                    visit_r[nx][ny] = True
                    q.append((nx,ny,color,t+1))
                    time[nx][ny] = t+1
            else:
                if visit_g[nx][ny]: continue
                if visit_r[nx][ny]:
                    if time[nx][ny]-1 == t:
                        cnt += 1
                        flower[nx][ny] = True
                else:
                    visit_g[nx][ny] = True
                    q.append((nx,ny,color,t+1))
                    time[nx][ny] = t+1

    answer.append(cnt)
    
answer = []
lands = combinations(possible, (g+r))

for land in lands:
    red_seeds = combinations(land, r)

    for red in red_seeds:
        result = []
        for i,j in land:
            if (i,j) in red:
                result.append((i,j,1,0))
            else:
                result.append((i,j,0,0))

        bfs(result)

print(max(answer))