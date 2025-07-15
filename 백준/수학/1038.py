from itertools import combinations

n = int(input())

nums = ['9','8','7','6','5','4','3','2','1','0']

li = list(combinations(nums, 2))

comb = []

for i in range(1,11):
    for li in list(combinations(nums, i)):
        comb.append(''.join(li))

answer = sorted(comb, key=lambda x:(len(x), x))

if n >= len(answer):
    print(-1)
else:
    print(answer[n])