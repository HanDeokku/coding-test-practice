# 쌓는것도 랜덤, 돌리는 것도 랜덤

# 백트래킹 하면서 90도 돌리고 


from itertools import permutations
from collections import deque

# 입력받기
maze = []
for _ in range(5):
    layer = [list(map(int, input().split())) for _ in range(5)]
    maze.append(layer)

# 회전 함수들
def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def rotate_270(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

# 최소 거리를 계산하는 함수
def func_with_order(new_maze, ar):
    rotated_maze = []

    for i in range(len(ar)):
        if ar[i] == 1:
            rotated_maze.append(rotate_90(new_maze[i]))
        elif ar[i] == 2:
            rotated_maze.append(rotate_180(new_maze[i]))
        elif ar[i] == 3:
            rotated_maze.append(rotate_270(new_maze[i]))
        else:
            rotated_maze.append(new_maze[i])

    start_end_pairs = [
        [(0, 0, 0), (4, 4, 4)],
        [(0, 0, 4), (4, 4, 0)],
        [(0, 4, 0), (4, 0, 4)],
        [(0, 4, 4), (4, 0, 0)]
    ]
    
    min_dist = float('inf')

    for start, end in start_end_pairs:
        sz, sx, sy = start
        ez, ex, ey = end

        if rotated_maze[sz][sx][sy] == 0 or rotated_maze[ez][ex][ey] == 0:
            continue

        dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        visit = [[[False] * 5 for _ in range(5)] for _ in range(5)]

        queue = deque([(sz, sx, sy)])
        visit[sz][sx][sy] = True

        dz = [0, 0, 0, 0, 1, -1]
        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]

        while queue:
            z, x, y = queue.popleft()

            for i in range(6):
                nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
                if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5 and not visit[nz][nx][ny] and rotated_maze[nz][nx][ny] == 1:
                    dist[nz][nx][ny] = dist[z][x][y] + 1
                    visit[nz][nx][ny] = True
                    queue.append((nz, nx, ny))

        if visit[ez][ex][ey]:
            if dist[ez][ex][ey] == 12:
                print(12)
                exit()
            min_dist = min(min_dist, dist[ez][ex][ey])

    return min_dist if min_dist != float('inf') else float('inf')

# 백트래킹 함수
def back(order, x, rr):
    global answer
    if x == 5:
        current_order_maze = [maze[idx] for idx in order]  # 판 순서 바꾸기
        answer = min(func_with_order(current_order_maze, rr), answer)
        return

    for i in range(4):  # 0: 회전 없음, 1: 90도, 2: 180도, 3: 270도
        rr[x] = i
        back(order, x + 1, rr)

# 초기 설정
answer = float('inf')
arr = [0] * 5

# 판 순서에 대해 모든 경우 탐색
orders = permutations([0, 1, 2, 3, 4])  # 판의 모든 순열 생성
for order in orders:
    back(order, 0, arr)

# 결과 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)