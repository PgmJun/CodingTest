from collections import deque
import sys
input = sys.stdin.readline


def bfs(p, visited, parentArr):
    visited[p] = True
    queue = deque([[graph[p],p]])
    while queue:
        parents, pNum = queue.popleft()
        for p in parents:
            if not visited[p]:
                queue.append([graph[p],p])
                parentArr[p] = pNum
                visited[pNum] = True


n = int(input())
graph = [[] for _ in range(n+1)]
parentArr = [1 for _ in range(n+1)]

for i in range(n-1):
    p,c = map(int,input().split())
    graph[c].append(p)
    graph[p].append(c)

visited = [False] * (n+1)
bfs(1,visited,parentArr)

for i in range(2,n+1):
    print(parentArr[i])