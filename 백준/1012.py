import sys
sys.setrecursionlimit(1000000)


def dfs(x, y, graph):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y, graph)
        dfs(x-1, y, graph)
        dfs(x, y+1, graph)
        dfs(x, y-1, graph)
        return True
    return False


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if dfs(i, j, graph) == True:
                    result += 1
    print(result)
