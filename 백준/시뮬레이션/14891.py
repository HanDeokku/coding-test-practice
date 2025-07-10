from collections import deque

cogwheel = []

for _ in range(4):
    s = list(input())
    wheel = deque(s)
    cogwheel.append(wheel)

k = int(input())

def rotateWheel(idx, v):
    global cogwheel
    odd = False
    if idx % 2 != 0:
        odd = True
    vArr = [0,0,0,0]
    if idx == 0:
        if cogwheel[idx][2] == cogwheel[1][6]:
            vArr[0] = 1
        else:
            if cogwheel[1][2] == cogwheel[2][6]:
                vArr[0] = 1
                vArr[1] = 1
            else:
                if cogwheel[2][2] == cogwheel[3][6]:
                    vArr[0] = 1
                    vArr[1] = 1
                    vArr[2] = 1
                else:
                    vArr[0] = 1
                    vArr[1] = 1
                    vArr[2] = 1
                    vArr[3] = 1
    elif idx == 3:
        if cogwheel[idx][6] == cogwheel[2][2]:
            vArr[3] = 1
        else:
            if cogwheel[1][2] == cogwheel[2][6]:
                vArr[3] = 1
                vArr[2] = 1
            else:
                if cogwheel[0][2] == cogwheel[1][6]:
                    vArr[3] = 1
                    vArr[2] = 1
                    vArr[1] = 1
                else:
                    vArr[0] = 1
                    vArr[1] = 1
                    vArr[2] = 1
                    vArr[3] = 1
    elif idx == 1:
        if cogwheel[idx][2] == cogwheel[2][6]:
            vArr[1] = 1
        else:
            if cogwheel[2][2] == cogwheel[3][6]:
                vArr[1] = 1
                vArr[2] = 1
            else:
                vArr[1] = 1
                vArr[2] = 1
                vArr[3] = 1
        
        if cogwheel[idx][6] != cogwheel[0][2]:
            vArr[0] = 1
    else:
        if cogwheel[idx][6] == cogwheel[1][2]:
            vArr[2] = 1
        else:
            if cogwheel[1][6] == cogwheel[0][2]:
                vArr[1] = 1
                vArr[2] = 1
            else:
                vArr[0] = 1
                vArr[1] = 1
                vArr[2] = 1
        
        if cogwheel[idx][2] != cogwheel[3][6]:
            vArr[3] = 1
    
    for i in range(4):
        if vArr[i]:
            if odd:
                if i % 2 != 0:
                    if v == 1:
                        tmp = cogwheel[i].pop()
                        cogwheel[i].appendleft(tmp)
                    else:
                        tmp = cogwheel[i].popleft()
                        cogwheel[i].append(tmp)
                else:
                    if v == 1:
                        tmp = cogwheel[i].popleft()
                        cogwheel[i].append(tmp)
                    else:
                        tmp = cogwheel[i].pop()
                        cogwheel[i].appendleft(tmp)
            else:
                if i % 2 == 0:
                    if v == 1:
                        tmp = cogwheel[i].pop()
                        cogwheel[i].appendleft(tmp)
                    else:
                        tmp = cogwheel[i].popleft()
                        cogwheel[i].append(tmp)
                else:
                    if v == 1:
                        tmp = cogwheel[i].popleft()
                        cogwheel[i].append(tmp)
                    else:
                        tmp = cogwheel[i].pop()
                        cogwheel[i].appendleft(tmp)

        

for _ in range(k):
    idx, v = map(int, input().split())
    i = idx-1
    rotateWheel(i, v)

answer = int(cogwheel[0][0]) * 1 + int(cogwheel[1][0]) * 2 + int(cogwheel[2][0]) * 4 + int(cogwheel[3][0]) * 8

print(answer)