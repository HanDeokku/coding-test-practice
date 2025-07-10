from collections import deque

t = int(input())

for _ in range(t):
    command = input()
    n = int(input())
    s = input().replace('[','').replace(']','')
    arr = deque()
    head = True
    check = True
    ar1 = s.split(',')

    for i in range(n):
        arr.append(ar1[i])

    for c in command:
        if c == 'R':
            head = not(head | False)

        else:
            if len(arr) > 0:
                if head:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                check = False
                break
    
    answer = '['
    if check:
        if head:
            while(arr):
                answer += (arr.popleft()+',')
        else:
            while(arr):
                answer += (arr.pop()+',')
        if answer == '[':
            answer += ']'
        else:
            answer = answer[:-1]+']'
        print(answer)
    else:
        print('error')