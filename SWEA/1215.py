def check_row(x, y, l, arr):
    check = True
    for i in range(l//2):
        if arr[x][y+i] != arr[x][y+(l-i-1)]:
            check = False
            break
    
    if check:
        return True
    else:
        return False

def check_col(x, y, l, arr):
    check = True
    for i in range(l//2):
        if arr[x+i][y] != arr[x+(l-i-1)][y]:
            check = False
            break
    
    if check:
        return True
    else:
        return False
    
cnt = 0

for case in range(1, 11):
    ln = int(input())
    matrix = [list(input()) for i in range(8)]
    for i in range(0, 8-ln+1):
        for j in range(8):
            if check_col(i, j, ln, matrix):
                cnt += 1

    for i in range(0, 8):
        for j in range(8 - ln + 1):
            if check_row(i, j, ln, matrix):
                cnt += 1

    print(f'#{case} {cnt}')