import sys
sys.setrecursionlimit(1000000)

t = int(input())

for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    
    visit = [False] * (n+1)

    team_ok = 0

    def dfs(x):
        global team_ok
        visit[x] = True
        next = students[x]
        team.append(x)

        if visit[next]:
            if next in team:
                team_ok += len(team[team.index(next):])
        else:
            dfs(next)

    for i in range(1,n+1):
        if not visit[i]:
            team = []
            dfs(i)
    
    answer = n - team_ok
    print(answer)
