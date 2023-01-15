# 정점의 갯수 N / 간선의 갯수 M / 시작점 V
from collections import deque


def dfs(v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited)


def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

visited = [False] * (n+1)
dfs(v, visited)
print()
bfs(v)
