s = input()

arr = [0] * 26

for c in s:
    n = ord(c)
    arr[n-97] += 1

for n in arr:
    print(n, end=' ')