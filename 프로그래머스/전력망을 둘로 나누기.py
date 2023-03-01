from collections import deque
from copy import deepcopy
import heapq


def bfs(s, n, graph):
    queue = deque([s])
    visited = [False] * (n+1)
    visited[s] = True
    cnt = 1

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                cnt += 1

    return cnt


def solution(n, wires):
    answer = []
    graph = [[] for _ in range(n+1)]

    for w1, w2 in wires:
        graph[w1].append(w2)
        graph[w2].append(w1)

    for i in range(1, n+1):
        for g in graph[i]:
            wireArr = deepcopy(graph)
            wireArr[i].remove(g)
            wireArr[g].remove(i)
            heapq.heappush(answer, abs(
                bfs(i, n, deepcopy(wireArr)) - bfs(g, n, deepcopy(wireArr))))

    return heapq.heappop(answer)
