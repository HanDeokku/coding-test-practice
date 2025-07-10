r, c = map(int, input().split())

originMap = []
afterMap = []

for i in range(r):
    line = list(input())
    originMap.append(line)
    afterMap.append(line.copy())


def checkSea(x, y):
    global r, c
    cnt = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if originMap[nx][ny] == '.':
                cnt += 1
        else:
            cnt += 1  # 지도 경계에 있는 경우 바다로 간주

    if cnt >= 3:
        return True
    else:
        return False

    

for i in range(r):
    for j in range(c):
        if (originMap[i][j] == 'X') and checkSea(i,j):
            afterMap[i][j] = '.'

min_row = 10
min_col = 10
max_row = 0
max_col = 0

for i in range(r):
    for j in range(c):
        if afterMap[i][j] == 'X':
            min_col = min(j, min_col)
            max_col = max(j, max_col)
            min_row = min(i, min_row)
            max_row = max(i, max_row)

for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
        print(afterMap[i][j], end='')
    print()