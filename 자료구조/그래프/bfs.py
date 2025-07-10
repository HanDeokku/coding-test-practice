from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        nbr = graph[vertex] - visited
        for v in nbr:
            visited.add(v)
            queue.append(v)