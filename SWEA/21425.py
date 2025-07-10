import sys
input = sys.stdin.readline()
a, b, n = map(int, input.split())

cnt = 0
# 작은거에 큰거를 더 해야함
if a < b:
    tmp = a
    a = b
    b = tmp
    # a가 더 큰거다
while n >= a and b <= n:
    if cnt % 2 == 0:
        b += a
        cnt += 1
    else:
        a += b
        cnt += 1

print(cnt)