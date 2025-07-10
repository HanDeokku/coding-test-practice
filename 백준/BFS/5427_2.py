from collections import deque

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    s_q, f_q = deque(), deque()
    s_v = [[False] * w for _ in range(h)]
    f_v = [[False] * w for _ in range(h)]
    sang_time = [[-1] * w for _ in range(h)]
    fire_time = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            value = building[i][j]
            if value == '@':
                s_q.append((i, j))
                s_v[i][j] = True
                sang_time[i][j] = 0
            elif value == '*':
                f_q.append((i, j))
                f_v[i][j] = True
                fire_time[i][j] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while f_q:
        x, y = f_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not f_v[nx][ny] and building[nx][ny] != '#':
                f_q.append((nx, ny))
                f_v[nx][ny] = True
                fire_time[nx][ny] = fire_time[x][y] + 1

    answer = float('inf')
    while s_q:
        x, y = s_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < h and 0 <= ny < w):
                answer = min(answer, sang_time[x][y] + 1)
                continue
            if not s_v[nx][ny] and building[nx][ny] == '.':
                if fire_time[nx][ny] != -1 and sang_time[x][y] + 1 >= fire_time[nx][ny]:
                    continue
                s_q.append((nx, ny))
                s_v[nx][ny] = True
                sang_time[nx][ny] = sang_time[x][y] + 1

    print('IMPOSSIBLE' if answer == float('inf') else answer)