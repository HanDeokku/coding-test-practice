import copy

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

direction = [0,1,2,3,4]

arr = [0]*5

answer = 0

def game(arr):
    sub = copy.deepcopy(board)
    for d in arr:
        visit = [[False] * n for _ in range(n)]
        if d == 0: # 제자리
            continue
        if d == 1: # 위로
            for i in range(n):
                for j in range(n):
                    if sub[i][j] != 0:
                        
                        index = -1
                        for k in range(i, -1, -1):
                            if k == 0:
                                if index == -1:
                                    break
                                
                                if sub[index][j] == sub[i][j]:
                                    sub[index][j] += sub[i][j]
                                    sub[i][j] = 0
                                    visit[index][j] = True
                                elif sub[index][j] == 0:
                                    sub[index][j] += sub[i][j]
                                    sub[i][j] = 0
                                
                                break

                            if sub[k-1][j] == sub[i][j] and not visit[k-1][j]:
                                index = k-1
                            elif sub[k-1][j] == 0:
                                index = k-1

                            
        elif d == 2: # 왼쪽으로
            for i in range(n):
                for j in range(n):
                    if sub[j][i] != 0:
                        
                        index = -1
                        for k in range(i, -1, -1):
                            if k == 0:
                                if index == -1:
                                    break

                                if sub[j][index] == sub[j][i]:
                                    sub[j][index] += sub[j][i]
                                    sub[j][i] = 0
                                    visit[j][index] = True
                                elif sub[j][index] == 0:
                                    sub[j][index] += sub[j][i]
                                    sub[j][i] = 0

                                break

                            if sub[j][k-1] == sub[j][i] and not visit[j][k-1]:
                                index = k-1
                            elif sub[j][k-1] == 0:
                                index = k-1
                            
                            
        elif d == 3: # 아래로
            for i in range(n-1, -1, -1):
                for j in range(n):
                    if sub[i][j] != 0:
                        
                        index = -1
                        for k in range(i, n):
                            if k == n-1:
                                if index == -1:
                                    break

                                if sub[index][j] == sub[index][j]:
                                    sub[index][j] += sub[i][j]
                                    sub[i][j] = 0
                                    visit[index][j] = True
                                elif sub[index][j] == 0:
                                    sub[index][j] += sub[i][j]
                                    sub[i][j] = 0
                                
                                break

                            if sub[k+1][j] == sub[i][j] and not visit[k+1][j]:
                                index = k+1
                            elif sub[k+1][j] == 0:
                                index = k+1
                            
                            


        else: # 오른쪽으로
            for i in range(n-1,-1,-1):
                for j in range(n):
                    if sub[j][i] != 0:
                        
                        index = -1
                        for k in range(i, -1, -1):
                            if k == n-1:
                                if index == -1:
                                    break
                                
                                if sub[j][index] == sub[j][i]:
                                    sub[j][index] += sub[j][i]
                                    sub[j][i] = 0
                                    visit[j][index] = True
                                elif sub[j][index] == 0:
                                    sub[j][index] += sub[j][i]
                                    sub[j][i] = 0
                                
                                break

                            if sub[j][k+1] == sub[j][i] and not visit[j][k+1]:
                                index = k+1
                            elif sub[j][k+1] == 0:
                                index = k+1

    result = 0
    for i in range(n):
        for j in range(n):
            result = max(sub[i][j], result)

    
    return result

def back(x):
    global answer
    if x == 5:
        answer = max(game(arr), answer)
        return
    
    for i in range(5):
        arr[x] = direction[i]
        back(x+1)

back(0)

print(answer)