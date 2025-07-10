n = int(input())

num = 1
answer = 0

for i in range(n, 0, -1):
    num = num * i
    if num % 10 == 0:
        answer += 1
        num = num // 10
    
print(answer)