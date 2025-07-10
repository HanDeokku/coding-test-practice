from itertools import combinations

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        elif city[i][j] == 1:
            home.append((i,j))

chicken_comb = list(combinations(chicken, m))

answer = 1000000

for comb in chicken_comb:
    comb_list = list(comb)
    city_dist = 0
    for x, y in home:
        home_dist = 100000
        for a, b in comb_list:
            home_dist = min(home_dist, (abs(x-a)+abs(y-b)))
        city_dist += home_dist
    
    answer = min(answer, city_dist)

print(answer)