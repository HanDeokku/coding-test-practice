e, s, m = map(int, input().split())

if e == 15:
    e = 0
if m == 19:
    m = 0

n = s

while True:
    if n % 15 == e and n % 19 == m:
        print(n)
        break
    else:
        n += 28
