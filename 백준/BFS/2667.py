from collections import deque

n = int(input())

apart = []

for _ in range(n):
    a = list(input())
    apart.append(a)

visit = [[False] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

count = 0
cnts = []

for i in range(n):
    for j in range(n):
        if apart[i][j] == '1' and not visit[i][j]:
            count += 1
            q = deque([(i,j)])
            visit[i][j] = True

            cnt = 1
            while q:
                x, y = q.popleft()
                
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y

                    if nx > n-1 or nx < 0 or ny > n-1 or ny < 0: continue
                    if visit[nx][ny]: continue
                    if apart[nx][ny] == '0': continue

                    visit[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1

            cnts.append(cnt)

cnts.sort()

print(count)
for c in cnts:
    print(c)

