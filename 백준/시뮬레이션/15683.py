import copy

n, m = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(n)]

wall = 0
cctv = []

for i in range(n):
    for j in range(m):
        kind = office[i][j]
        if kind != 0 and kind != 6:
            if kind == 1:
                cctv.append([kind, 4])
            elif kind == 2:
                cctv.append([kind,2])
            elif kind == 3:
                cctv.append([kind,4])
            elif kind == 4:
                cctv.append([kind,4])
            else:
                cctv.append([kind,1])
        
        if kind == 6:
            wall += 1

c = len(cctv)

arr = [[0] * 2 for _ in range(c)]

answer = 100

def func(array):
    blindSpot = copy.deepcopy(office)
    index = 0

    x, y = array[index]
    check = False

    for i in range(n):
        if check:
            break
        for j in range(m):
            if index == c:
                check = True
                break
            x, y = array[index]

            if blindSpot[i][j] == x:
                if x == 1:
                    if y == 1:
                        for k in range(j+1, m):
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    elif y == 2:
                        for k in range(i+1, n):
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                    elif y == 3:
                        for k in range(j-1, -1, -1):
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    else:
                        for k in range(i-1, -1, -1):
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                elif x == 2:
                    if y == 1:
                        for k in range(j-1, -1, -1): # 왼쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        for k in range(j+1, m): # 오른쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    else:
                        for k in range(i-1, -1, -1): # 위쪽
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                        
                        for k in range(i+1, n): # 아래
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                elif x == 3:
                    if y == 1:
                        for k in range(i-1, -1, -1): # 위쪽
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                    
                        for k in range(j+1, m): # 오른쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    elif y == 2:
                        for k in range(j+1, m): # 오른쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        
                        for k in range(i+1, n): # 아래
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                    elif y == 3:
                        for k in range(i+1, n): # 아래
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                        
                        for k in range(j-1, -1, -1): # 왼쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    else:
                        for k in range(j-1, -1, -1): # 왼쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        for k in range(i-1, -1, -1): # 위쪽
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                elif x == 4:
                    if y == 1:
                        for k in range(j-1, -1, -1): # 왼쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        for k in range(i-1, -1, -1): # 위쪽
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                        for k in range(j+1, m): # 오른쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    elif y == 2:
                        for k in range(i-1, -1, -1): # 위쪽
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                        for k in range(j+1, m): # 오른쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        for k in range(i+1, n): # 아래
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                    elif y == 3:
                        for k in range(j+1, m): # 오른쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        for k in range(i+1, n): # 아래
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                        for k in range(j-1, -1, -1): # 왼쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                    else:
                        for k in range(j-1, -1, -1): # 왼쪽
                            if blindSpot[i][k] == 0:
                                blindSpot[i][k] = -1
                            elif blindSpot[i][k] == 6:
                                break
                            else:
                                continue
                        for k in range(i+1, n): # 아래
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                        for k in range(i-1, -1, -1): # 위쪽
                            if blindSpot[k][j] == 0:
                                blindSpot[k][j] = -1
                            elif blindSpot[k][j] == 6:
                                break
                            else:
                                continue
                else:
                    for k in range(j-1, -1, -1): # 왼쪽
                        if blindSpot[i][k] == 0:
                            blindSpot[i][k] = -1
                        elif blindSpot[i][k] == 6:
                            break
                        else:
                            continue
                    for k in range(i+1, n): # 아래
                        if blindSpot[k][j] == 0:
                            blindSpot[k][j] = -1
                        elif blindSpot[k][j] == 6:
                            break
                        else:
                            continue
                    for k in range(i-1, -1, -1): # 위쪽
                        if blindSpot[k][j] == 0:
                            blindSpot[k][j] = -1
                        elif blindSpot[k][j] == 6:
                            break
                        else:
                            continue
                    for k in range(j+1, m): # 오른쪽
                        if blindSpot[i][k] == 0:
                            blindSpot[i][k] = -1
                        elif blindSpot[i][k] == 6:
                            break
                        else:
                            continue

                index += 1

    count = 0

    for i in range(n):
        for j in range(m):
            if blindSpot[i][j] == 0:
                count += 1

    return count

def back(x):
    global answer
    if x == c:
        num = func(arr)
        answer = min(answer, num)
        return
    
    for i in range(1, cctv[x][1]+1):
        arr[x][0] = cctv[x][0]
        arr[x][1] = i
        back(x+1)

if c != 0:
    back(0)
else:
    answer = n*m - wall

print(answer)