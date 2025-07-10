t = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(t):
    arr_input = list(map(int, input().split()))
    n = arr_input[0]
    arr = arr_input[1:]

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            a = max(arr[i], arr[j])
            b = min(arr[i], arr[j])
            answer += gcd(a, b)
    
    print(answer)