from collections import deque

for _ in range(2):
    case = int(input())
    nums = list(map(int, input().split()))
    dq = deque()
    for num in nums:
        dq.append(num)

    n = 1
    while True:
        if n > 5:
            n = 1
        num = dq.popleft()
        num = num - n
        if num <= 0:
            num = 0
            dq.append(num)
            break
        else:
            dq.append(num)
            n += 1
    
    print(f'#{case}', end=' ')
    for d in dq:
        print(d, end=' ')