t = int(input())

def count_flys(x, y, m, arr):
    count = 0
    for i in range(x, x+m):
        for j in range(y, y+m):
            count += int(arr[i][j])
    
    return count


for case in range(1, t+1):
    n, m = map(int, input().split())
    flys = [] 
    for i in range(n):
        f = input().split()
        flys.append(f)
    
    answer = 0
    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            answer = max(answer, count_flys(i, j, m, flys))

    print(f'#{case} {answer}')