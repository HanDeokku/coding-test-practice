from itertools import permutations
from collections import deque

dx, dy = [1,0,-1,0], [0,1,0,-1]
dz = [1,-1]

answer = []

# 회전 함수들
def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def rotate_270(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def bfs(arr):
    new_maze = []

    for rotation, layer_idx in arr:
        layer = rotated_maze[layer_idx][rotation]
        new_maze.append(layer)

    if new_maze[0][0][0] == 0 or new_maze[4][4][4] == 0:
        return

    q = deque()
    q.append((0,0,0))
    dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visit = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visit[0][0][0] = True

    while q:
        z,x,y = q.popleft()

        if z == 4 and x == 4 and y == 4:
            answer.append(dist[z][x][y])
            if dist[z][x][y] == 12:
                print(12)
                exit()
            return

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx > 4 or nx < 0 or ny > 4 or ny < 0: continue
            if new_maze[z][nx][ny] == 0: continue
            if visit[z][nx][ny]: continue
            dist[z][nx][ny] = dist[z][x][y] + 1
            visit[z][nx][ny] = True
            q.append((z,nx,ny))
        
        for i in range(2):
            nz = dz[i] + z

            if nz > 4 or nz < 0: continue
            if new_maze[nz][x][y] == 0: continue
            if visit[nz][x][y]: continue
            dist[nz][x][y] = dist[z][x][y] + 1
            visit[nz][x][y] = True
            q.append((nz,x,y))

maze = []
for _ in range(5):
    layer = [list(map(int, input().split())) for _ in range(5)]
    maze.append(layer)

idx = [0,1,2,3,4]

rotated_maze = [[[] for _ in range(4)] for _ in range(5)]

for i in range(5):
    rotated_maze[i][0] = maze[i]
    rotated_maze[i][1] = rotate_90(maze[i])
    rotated_maze[i][2] = rotate_180(maze[i])
    rotated_maze[i][3] = rotate_270(maze[i])

order = list(permutations(idx, 5))

for a1 in range(4):
    for b1 in range(4):
        for c1 in range(4):
            for d1 in range(4):
                for e1 in range(4):
                    for a2, b2, c2, d2, e2 in order:
                        rotate_order = [(a1,a2),(b1,b2),(c1,c2),(d1,d2),(e1,e2)]
                        bfs(rotate_order)

if answer:
    print(min(answer))
else:
    print(-1)