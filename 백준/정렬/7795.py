import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    answer = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] > b[j]:
                answer += (len(b) - j)
                break
    
    print(answer)
