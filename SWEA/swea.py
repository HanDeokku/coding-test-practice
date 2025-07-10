for case in range(1,4):
    n = int(input())
    building = list(map(int, input().split()))
    answer = 0
    for i in range(2,n-2):
        left = max(building[i-2], building[i-1])
        right = max(building[i+2], building[i+1])
        if left < building[i] and right < building[i]:
            answer += building[i] - max(left, right)
    
    print(f'#{case} {answer}')