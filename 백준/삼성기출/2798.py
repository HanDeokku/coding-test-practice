n, m = map(int, input().split())

cards = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i :
                continue 
            sum_c = cards[i] + cards[j] + cards[k]
            if sum_c <= m:
                answer = max(answer, sum_c)

print(answer)