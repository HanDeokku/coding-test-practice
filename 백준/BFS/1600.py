from collections import deque

k = int(input())
w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]

dx1 = [1, 2, 2, 1, -1, -2, -2, -1]
dy1 = [2, 1, -1, -2, -2, -1, 1, 2]

dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]

visited = [[[False] * w for _ in range(h)] for _ in range(k+1)]
action = [[[0] * w for _ in range(h)] for _ in range(k+1)]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = True

while queue:
    a, x, y = queue.popleft()

    if a < k:
        for i in range(8):
            nx, ny = x + dx1[i], y + dy1[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[a+1][nx][ny] and board[nx][ny] == 0:
                visited[a+1][nx][ny] = True
                action[a+1][nx][ny] = action[a][x][y] + 1
                queue.append((a+1, nx, ny))

    for i in range(4):
        nx, ny = x + dx2[i], y + dy2[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[a][nx][ny] and board[nx][ny] == 0:
            visited[a][nx][ny] = True
            action[a][nx][ny] = action[a][x][y] + 1
            queue.append((a, nx, ny))

answer = 1000000000
for i in range(k+1):
    if not visited[i][h-1][w-1]: continue
    answer = min(answer, action[i][h-1][w-1])

if answer == 1000000000:
    print(-1)
else:
    print(answer)
