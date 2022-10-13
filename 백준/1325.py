from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    cnt = 0
    visited = [False]*(n+1)
    visited[start] = True
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                cnt += 1
    return cnt
                
n,m = map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().rstrip().split())
    graph[y].append(x)

result = []
max_cnt = -sys.maxsize

for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)

print(*result)