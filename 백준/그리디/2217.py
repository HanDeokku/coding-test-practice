import sys
input = sys.stdin.readline

rope = []
n = int(input())

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
answer = 0

for i in range(n):
    answer = max(answer, rope[i]*(i+1))

print(answer)