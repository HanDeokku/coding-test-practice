import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    n = y-x
    i = 1
    cnt = 0
    check = False
    while True:
        for _ in range(2):
            n -= i
            cnt += 1
            if n <= i:
                if not n == 0: cnt += 1
                check = True
                break
        
        if check:
            break
        
        i += 1
    
    print(cnt)