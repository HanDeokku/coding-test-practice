# d[i][j] = j만큼 연속해서 i까지 계단을 밟았을 때 최대값
# d[k][1] = max(d[k-2][2], d[k-2][1]) + s[k]
# d[k][2] = d[k-1][1] + s[k]

import sys
input = sys.stdin.readline

n = int(input())

s = [0]

for _ in range(n):
    s.append(int(input()))

d = [[0] * 3 for _ in range(n+1)]

d[1][1] = s[1]
d[0][1] = 0
d[0][2] = 0
d[1][2] = 0

for i in range(2,n+1):
    d[i][1] = max(d[i-2][2], d[i-2][1]) + s[i]
    d[i][2] = d[i-1][1] + s[i]

print(max(d[n][2], d[n][1]))