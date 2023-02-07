from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        s = queue.popleft()
        for v in graph[s]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)
