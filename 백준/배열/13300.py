n, k = map(int, input().split())
students = [[0] * 2 for _ in range(6)]

for i in range(n):
    s, g = map(int, input().split())
    students[g-1][s] += 1

room = 0

for i in range(6):
    for j in range(2):
        num = students[i][j]
        if num % k == 0:
            room += num // k
        else:
            room += (num // k) + 1

print(room)