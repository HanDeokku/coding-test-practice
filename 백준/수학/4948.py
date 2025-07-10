import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    m = 2 * n

    answer = 0

    for i in range(n+1, m+1):
        check = True
        for j in range(2, i+1):
            if j * j > i:
                break
            if i % j == 0:
                check = False
                break
        
        if check:
            answer += 1

    print(answer)