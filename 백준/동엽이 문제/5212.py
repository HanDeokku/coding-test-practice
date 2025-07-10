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
    if x - 1 >= 0:
        if originMap[x-1][y] == '.':
            cnt += 1
    if x + 1 < r:
        if originMap[x+1][y] == '.':
            cnt += 1
    if y - 1 >= 0:
        if originMap[x][y-1] == '.':
            cnt += 1
    if y + 1 < c:
        if originMap[x][y+1] == '.':
            cnt += 1
    if (y == 0) or (x == 0) or (x == r-1) or (y == c-1):
        cnt += 1
    # if ((y == 0) and (x == 0)) or ((y == c-1) and (x  == 0)) or ((y == 0) and (x == r-1)) or ((y == c-1) and (x == r-1)): 
    #     cnt += 1
    if (y == 0) and (x == 0):
        cnt += 1
    if (y == c-1) and (x == 0):
        cnt += 1
    if (y == 0) and (x == r-1):
        cnt += 1
    if (y == c-1) and (x == r-1):
        cnt += 1
    
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