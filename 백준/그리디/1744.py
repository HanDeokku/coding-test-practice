n = int(input())

a1 = []
a2 = []
a3 = []

for i in range(n):
    num = int(input())
    if num <= 0:
        a1.append(num)
    elif num == 1:
        a3.append(num)
    else:
        a2.append(num)

a1.sort()
a2.sort(reverse=True)

answer = 0

for i in range(0,len(a1),2):
    if i+1 < len(a1):
        answer += (a1[i] * a1[i+1])
    else:
        answer += a1[i]

for i in range(0,len(a2),2):
    if i+1 < len(a2):
        answer += (a2[i] * a2[i+1])
    else:
        answer += a2[i]

answer += len(a3)

print(answer)