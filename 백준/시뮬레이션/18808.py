n, m, k = map(int, input().split())

laptop = [[0] * m for _ in range(n)]
sticker = []

def makeV(v, arr):
    if v == 0:
        return arr
    elif v == 1:
        r = len(arr[0]) # 5
        c = len(arr) # 2
        new_arr = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                new_arr[i][j] = arr[c-j-1][i]
        return new_arr
    elif v == 2:
        r = len(arr) # 2
        c = len(arr[0]) # 5
        new_arr = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                new_arr[i][j] = arr[r-i-1][c-j-1]
        return new_arr
    else:
        r = len(arr[0]) # 5
        c = len(arr) # 2
        new_arr = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                new_arr[i][j] = arr[j][r-i-1]
        return new_arr

def check(arr):
    r = len(arr) # 5
    c = len(arr[0]) # 2
    for i in range(0, n-r+1):
        for j in range(0, m-c+1):
            bp = False
            for k in range(r):
                if bp:
                    break
                for l in range(c):
                    if arr[k][l] and laptop[i+k][j+l]:
                        bp = True
                        break
            if not bp:
                return (True, i, j)

    return (False, -1, -1)

def draw(arr, x, y):
    global laptop
    r = len(arr)
    c = len(arr[0])
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                laptop[x+i][y+j] = 1

    return

for i in range(k):
    r, c = map(int, input().split())
    add = [list(map(int, input().split())) for _ in range(r)]
    sticker.append(add)

for i in range(k):
    for j in range(4):
        checkArr = makeV(j, sticker[i])
        checkPoint, x, y = check(checkArr)
        if checkPoint:
            draw(checkArr, x, y)
            break

cnt = 0
for i in range(n):
    for j in range(m):
        if laptop[i][j] == 1:
            cnt += 1

print(cnt)