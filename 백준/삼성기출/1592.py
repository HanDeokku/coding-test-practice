# 공을 M번 받은 사람이 있으면 종료
# 자기가 홀수번 받았으면 시계 방항으로 L번째에 토스
# 짝수번 받았으면 반시계 방향으로
# N은 몇명인지, M, L

# 공을 총 몇 번 던지는지.

n, m , l = map(int, input().split())

count = [0] * n
count[0] += 1

index = 0
answer = 0
while(max(count) != m):
    if count[index] % 2 == 0:
        index = index + l
    else:
        index = index - l

    if index > n-1:
        index = index - n
    elif index < 0:
        index = index + n 

    count[index] += 1
    answer += 1

print(answer)