# 위상 정렬

def topologicla_sort_AM(vertax, graph):
    n = len(vertax)
    inDeg = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                inDeg[j] += 1

    vlist = []
    for i in range(n):
        if inDeg[i] == 0:
            vlist.append(i)

    while len(vlist) > 0:
        v = vlist.pop()
        print(vertax[v], end=' ')

        for u in range(n):
            if v != u and graph[v][u] > 0:
                inDeg[u] -= 1
                if inDeg[u] == 0:
                    vlist.append(u)
