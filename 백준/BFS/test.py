from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

num = 1
world = [[[0] * 2 for _ in range(n)] for _ in range(n)]
world_q = deque()


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and world[i][j][0] == 0:
            queue = deque([(i, j)])
            world_q.append((i, j, -num))
            world[i][j][0] = -num
            world[i][j][1] = -num

            while queue:
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and world[nx][ny][0] == 0:
                        world[nx][ny][0] = -num
                        world[nx][ny][1] = -num
                        queue.append((nx, ny))
                        world_q.append((nx, ny, -num))

            num += 1
print(world)