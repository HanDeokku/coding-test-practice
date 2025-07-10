from collections import deque

cogwheel = []

for _ in range(4):
    s = list(input())
    wheel = deque(s)
    cogwheel.append(wheel)

k = int(input())

def rotateWheel(idx, v):
    global cogwheel
    if idx == 0:
        # 1번과 2번이 서로 같을 때
        if cogwheel[idx][2] == cogwheel[1][6]:
            # 1번 돌리기
            if v == 1: # 시계
                tmp = cogwheel[idx].pop()
                cogwheel[idx].appendleft(tmp)
            else: # 반시계
                tmp = cogwheel[idx].popleft()
                cogwheel[idx].append(tmp)
        # 1번과 2번이 서로 다를 때
        else: 
            # 2번과 3번이 서로 같을 때
            if cogwheel[1][2] == cogwheel[2][6]:
                # 1번 2번 돌리기
                if v == 1: # 시계
                    tmp = cogwheel[idx].pop()
                    cogwheel[idx].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[idx].popleft()
                    cogwheel[idx].append(tmp)
                
                if v == 1: # 반시계
                    tmp = cogwheel[1].popleft()
                    cogwheel[1].append(tmp)
                else: # 시계
                    tmp = cogwheel[1].pop()
                    cogwheel[1].appendleft(tmp)
            # 2번과 3번이 서로 다를 때
            else:
                # 3번 4번 같을 때
                if cogwheel[2][2] == cogwheel[3][6]:
                    # 1번 2번 3번 돌리기
                    if v == 1: # 시계
                        tmp = cogwheel[idx].pop()
                        cogwheel[idx].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[idx].popleft()
                        cogwheel[idx].append(tmp)
                
                    if v == 1: # 반시계
                        tmp = cogwheel[1].popleft()
                        cogwheel[1].append(tmp)
                    else: # 시계
                        tmp = cogwheel[1].pop()
                        cogwheel[1].appendleft(tmp)
                    
                    if v == 1: # 시계
                        tmp = cogwheel[2].pop()
                        cogwheel[2].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[2].popleft()
                        cogwheel[2].append(tmp)
                else:
                    # 1번 2번 3번 4번 돌리기
                    if v == 1: # 시계
                        tmp = cogwheel[idx].pop()
                        cogwheel[idx].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[idx].popleft()
                        cogwheel[idx].append(tmp)
                
                    if v == 1: # 반시계
                        tmp = cogwheel[1].popleft()
                        cogwheel[1].append(tmp)
                    else: # 시계
                        tmp = cogwheel[1].pop()
                        cogwheel[1].appendleft(tmp)
                    
                    if v == 1: # 시계
                        tmp = cogwheel[2].pop()
                        cogwheel[2].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[2].popleft()
                        cogwheel[2].append(tmp)
                    
                    if v == 1: # 반시계
                        tmp = cogwheel[3].popleft()
                        cogwheel[3].append(tmp)
                    else: # 시계
                        tmp = cogwheel[3].pop()
                        cogwheel[3].appendleft(tmp)

    elif idx == 3:
        # 4번과 3번이 서로 같을 때
        if cogwheel[idx][6] == cogwheel[2][2]:
            if v == 1: # 시계
                tmp = cogwheel[idx].pop()
                cogwheel[idx].appendleft(tmp)
            else: # 반시계
                tmp = cogwheel[idx].popleft()
                cogwheel[idx].append(tmp)
        # 4번과 3번이 서로 다를 때
        else: 
            # 2번과 3번이 서로 같을 때
            if cogwheel[1][2] == cogwheel[2][6]:
                # 4번 3번 돌리기
                if v == 1: # 시계
                    tmp = cogwheel[idx].pop()
                    cogwheel[idx].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[idx].popleft()
                    cogwheel[idx].append(tmp)
                
                if v == 1: # 반시계
                    tmp = cogwheel[2].popleft()
                    cogwheel[2].append(tmp)
                else: # 시계
                    tmp = cogwheel[2].pop()
                    cogwheel[2].appendleft(tmp)
            # 2번과 3번이 서로 다를 때
            else:
                if cogwheel[0][2] == cogwheel[1][6]:
                    # 4번 3번 2번 돌리기
                    if v == 1: # 시계
                        tmp = cogwheel[idx].pop()
                        cogwheel[idx].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[idx].popleft()
                        cogwheel[idx].append(tmp)
                
                    if v == 1: # 반시계
                        tmp = cogwheel[2].popleft()
                        cogwheel[2].append(tmp)
                    else: # 시계
                        tmp = cogwheel[2].pop()
                        cogwheel[2].appendleft(tmp)
                    
                    if v == 1: # 시계
                        tmp = cogwheel[1].pop()
                        cogwheel[1].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[1].popleft()
                        cogwheel[1].append(tmp)
                else:
                    # 1번 2번 3번 4번 돌리기
                    if v == 1: # 시계
                        tmp = cogwheel[idx].pop()
                        cogwheel[idx].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[idx].popleft()
                        cogwheel[idx].append(tmp)
                
                    if v == 1: # 반시계
                        tmp = cogwheel[2].popleft()
                        cogwheel[2].append(tmp)
                    else: # 시계
                        tmp = cogwheel[2].pop()
                        cogwheel[2].appendleft(tmp)
                    
                    if v == 1: # 시계
                        tmp = cogwheel[1].pop()
                        cogwheel[1].appendleft(tmp)
                    else: # 반시계
                        tmp = cogwheel[1].popleft()
                        cogwheel[1].append(tmp)
                    
                    if v == 1: # 반시계
                        tmp = cogwheel[0].popleft()
                        cogwheel[0].append(tmp)
                    else: # 시계
                        tmp = cogwheel[0].pop()
                        cogwheel[0].appendleft(tmp)
                        
    elif idx == 1:
        # 2번 3번 같을 때
        if cogwheel[idx][2] == cogwheel[2][6]:
            # 2번 돌리기
            if v == 1: # 시계
                tmp = cogwheel[idx].pop()
                cogwheel[idx].appendleft(tmp)
            else: # 반시계
                tmp = cogwheel[idx].popleft()
                cogwheel[idx].append(tmp)
        # 2번 3번 다를 때
        else:
            # 3번 4번 같을 때
            if cogwheel[2][2] == cogwheel[3][6]:
                # 2번 3번 돌리기
                if v == 1: # 시계
                    tmp = cogwheel[idx].pop()
                    cogwheel[idx].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[idx].popleft()
                    cogwheel[idx].append(tmp)
                
                if v == 1: # 반시계
                    tmp = cogwheel[2].popleft()
                    cogwheel[2].append(tmp)
                else: # 반시계
                    tmp = cogwheel[2].pop()
                    cogwheel[2].appendleft(tmp)
            # 3번 4번 다를 때
            else:
                # 2번 3번 4번 돌리기
                if v == 1: # 시계
                    tmp = cogwheel[idx].pop()
                    cogwheel[idx].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[idx].popleft()
                    cogwheel[idx].append(tmp)
                
                if v == 1: # 반시계
                    tmp = cogwheel[2].popleft()
                    cogwheel[2].append(tmp)
                else: # 반시계
                    tmp = cogwheel[2].pop()
                    cogwheel[2].appendleft(tmp)

                if v == 1: # 시계
                    tmp = cogwheel[3].pop()
                    cogwheel[3].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[3].popleft()
                    cogwheel[3].append(tmp)

        # 1번 확인하기
        if cogwheel[idx][6] != cogwheel[0][2]:
            if v == 1: # 반시계
                tmp = cogwheel[0].popleft()
                cogwheel[0].append(tmp)
            else: # 시계
                tmp = cogwheel[0].pop()
                cogwheel[0].appendleft(tmp)
    
    else: 
        # 2번 3번 같을 때
        if cogwheel[idx][6] == cogwheel[1][2]:
            # 3번 돌리기
            if v == 1: # 시계
                tmp = cogwheel[idx].pop()
                cogwheel[idx].appendleft(tmp)
            else: # 반시계
                tmp = cogwheel[idx].popleft()
                cogwheel[idx].append(tmp)
        # 2번 3번 다를 때
        else:
            # 1번 2번 같을 때
            if cogwheel[0][2] == cogwheel[1][6]:
                # 2번 3번 돌리기
                if v == 1: # 시계
                    tmp = cogwheel[idx].pop()
                    cogwheel[idx].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[idx].popleft()
                    cogwheel[idx].append(tmp)
                
                if v == 1: # 반시계
                    tmp = cogwheel[1].popleft()
                    cogwheel[1].append(tmp)
                else: # 반시계
                    tmp = cogwheel[1].pop()
                    cogwheel[1].appendleft(tmp)
            # 1번 2번 다를 때
            else:
                # 1번 2번 3번 돌리기
                if v == 1: # 시계
                    tmp = cogwheel[idx].pop()
                    cogwheel[idx].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[idx].popleft()
                    cogwheel[idx].append(tmp)
                
                if v == 1: # 반시계
                    tmp = cogwheel[1].popleft()
                    cogwheel[1].append(tmp)
                else: # 반시계
                    tmp = cogwheel[1].pop()
                    cogwheel[1].appendleft(tmp)

                if v == 1: # 시계
                    tmp = cogwheel[0].pop()
                    cogwheel[0].appendleft(tmp)
                else: # 반시계
                    tmp = cogwheel[0].popleft()
                    cogwheel[0].append(tmp)

        # 4번 확인하기
        if cogwheel[idx][2] != cogwheel[3][6]:
            if v == 1: # 반시계
                tmp = cogwheel[3].popleft()
                cogwheel[3].append(tmp)
            else: # 시계
                tmp = cogwheel[3].pop()
                cogwheel[3].appendleft(tmp)

for _ in range(k):
    idx, v = map(int, input().split())
    i = idx-1
    rotateWheel(i, v)

answer = int(cogwheel[0][0]) * 1 + int(cogwheel[1][0]) * 2 + int(cogwheel[2][0]) * 4 + int(cogwheel[3][0]) * 8

print(answer)