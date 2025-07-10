import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    
    mp = 0
    answer = 0
    for i in range(n-1, -1, -1):
        if stock[i] > mp:
            mp = stock[i]
        else:
            answer += (mp-stock[i])

    print(answer)