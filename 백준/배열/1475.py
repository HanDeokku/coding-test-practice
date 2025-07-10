s = input()

arr = [0] * 10

for n in s:
    if n == '6' or n == '9':
        if arr[6] == arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(n)] += 1

print(max(arr))

