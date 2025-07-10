n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

moveArr = list(map(int, input().split()))

dice = [0,0,0,0,0,0]

def checkAndWork(x,y):
    global dice
    if board[x][y] > 0:
        dice[5] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[5]

    print(dice[0])

for move in moveArr:
    if move == 1:
        if y+1>m-1: continue

        # 0->2 2->5 5->3 3->0
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp

        y += 1
        checkAndWork(x,y)

    elif move == 2:
        if y-1<0: continue
        # 0->3->5->2->0
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = tmp

        y -= 1
        checkAndWork(x,y)

    elif move == 3:
        if x-1<0: continue
        # 0->1->5->4->0
        tmp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = tmp

        x -= 1
        checkAndWork(x,y)

    else:
        if x+1>n-1: continue
        # 0->4->5->1->0
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp

        x += 1
        checkAndWork(x,y)


