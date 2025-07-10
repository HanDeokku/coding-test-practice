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

for _ in range(1, 2):
    case = int(input())
    matrix = [list(input()) for i in range(100)]
    cnt = 0
    ln = 100
    while(ln):
        check = True
        for i in range(0, 100-ln+1):
            for j in range(100):
                if check_col(i, j, ln, matrix):
                    check = False

        for i in range(0, 100):
            for j in range(100 - ln + 1):
                if check_row(i, j, ln, matrix):
                    check = False
        
        if check:
            ln -= 1
        else:
            break

    print(f'#{case} {ln}')