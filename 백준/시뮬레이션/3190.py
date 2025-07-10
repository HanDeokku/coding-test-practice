from collections import deque

n = int(input())
k = int(input())
apple = [[False] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    apple[x-1][y-1] = True

l = int(input())
direction = {}
for _ in range(l):
    t, d = input().split()
    direction[int(t)] = d

# 방향: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_idx = 0

snake = deque()
snake.append((0, 0))
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[dir_idx]
    ny = y + dy[dir_idx]

    if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
        print(time)
        break

    snake.append((nx, ny))
    visited[nx][ny] = True

    if apple[nx][ny]:
        apple[nx][ny] = False
    else:
        tx, ty = snake.popleft()
        visited[tx][ty] = False

    if time in direction:
        if direction[time] == 'D':
            dir_idx = (dir_idx + 1) % 4
        else:  # 'L'
            dir_idx = (dir_idx - 1) % 4

    x, y = nx, ny