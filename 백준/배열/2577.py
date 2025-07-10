a = int(input())
b = int(input())
c = int(input())

s = str(a * b * c)

arr = [0] * 10

for n in s:
    arr[int(n)] += 1

for i in range(10):
    print(arr[i])