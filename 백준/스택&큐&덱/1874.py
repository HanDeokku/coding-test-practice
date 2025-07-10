n = int(input())

s1 = []

now = 1
answer = []
check = True

for _ in range(n):
    num = int(input())

    while(now <= num):
        s1.append(now)
        answer.append('+')
        now += 1
    if s1[-1] == num:
        s1.pop()
        answer.append('-')
    else:
        check = False
        break

if check:
    for a in answer:
        print(a)
else:
    print('NO')