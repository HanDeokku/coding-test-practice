arr = []
n = int(input())
for _ in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

for i in range(n):
    print(arr[i])