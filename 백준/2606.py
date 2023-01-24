from collections import deque


def bfs(start, visited):
    queue = deque([start])
    cnt = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                cnt += 1
    print(cnt)


n = int(input())  # 컴퓨터의 수
conn = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
visited = [False] * (n+1)  # 방문 체크

graph = [[] for _ in range(n+1)]  # 연결 관계 그래프
for i in range(1, conn+1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
print(graph)
bfs(1, visited)
