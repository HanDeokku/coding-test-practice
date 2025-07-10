from collections import deque

n, m = map(int, input().split())
glacier = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def melt_glacier():
    melted = deque()
    remain = deque()
    
    for i in range(n):
        for j in range(m):
            if glacier[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and glacier[nx][ny] == 0:
                        cnt += 1
                
                if glacier[i][j] <= cnt:
                    melted.append((i, j))
                else:
                    glacier[i][j] -= cnt
                    remain.append((i, j))
    
    for x, y in melted:
        glacier[x][y] = 0
    
    return remain

def is_separated(queue):
    visited = [[False] * m for _ in range(n)]
    x, y = queue[0]
    visited[x][y] = True
    
    q = deque([(x, y)])
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and glacier[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    
    return count != len(queue)

years = 0
while True:
    queue = melt_glacier()
    if not queue:
        print(0)
        break
    
    years += 1
    if is_separated(queue):
        print(years)
        break
