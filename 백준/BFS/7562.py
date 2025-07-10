from collections import deque

t = int(input())

for _ in range(t):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    visit = [[False] * l for _ in range(l)]
    s_x, s_y = map(int, input().split())
    t_x, t_y = map(int, input().split())

    queue = deque()

    queue.append((s_x,s_y))
    visit[s_x][s_y] = True

    cnt = 0
    dx = [2,2,1,1,-1,-1,-2,-2]
    dy = [1,-1,2,-2,2,-2,1,-1]

    while queue:
        x, y = queue.popleft()
        if x == t_x and y == t_y: break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > l-1 or nx < 0 or ny > l-1 or ny < 0: continue
            if visit[nx][ny]: continue
            chess[nx][ny] = chess[x][y] + 1
            queue.append((nx,ny))
            visit[nx][ny] = True
    
    print(chess[t_x][t_y])