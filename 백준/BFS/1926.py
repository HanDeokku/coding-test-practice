from collections import deque

n, m = map(int, input().split())

pictures = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

def BFS(i, j, pictures, visit):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = len(pictures)
    m = len(pictures[0])

    queue = deque([(i, j)])
    visit[i][j] = True

    size = 0
    while queue:
        x, y = queue.popleft()
        size += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1: continue
            if visit[nx][ny]: continue
            if pictures[nx][ny] == 0 : continue
            queue.append((nx, ny))
            visit[nx][ny] = True
    
    return size

cnt = 0
sizes = []
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1 and not visit[i][j]:
            cnt += 1
            sizes.append(BFS(i, j, pictures, visit))

print(cnt)
if len(sizes) == 0:
    print(0)
else:
    print(max(sizes))