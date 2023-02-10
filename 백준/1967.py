import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(node, length, maxLength):
    maxLength = max(maxLength, length)
    result.append(maxLength)
    for n, l in graph[node]:
        if not visited[n]:
            visited[n] = True
            dfs(n, l+length, maxLength)


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, g, l = map(int, input().split())
    graph[s].append([g, l])
    graph[g].append([s, l])

result = []
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    visited[i] = True
    dfs(i, 0, -1)

print(max(result))
