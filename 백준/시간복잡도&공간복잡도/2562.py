max_num = 0
answer = 0
for i in range(1, 10):
    n = int(input())
    if n > max_num:
        max_num = n
        answer = i

print(max_num)
print(answer)
