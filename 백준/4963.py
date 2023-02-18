import sys
sys.setrecursionlimit(int(1e6))


def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if graph[x][y] == 0:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        dfs(x-1, y-1)
        dfs(x+1, y+1)


while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
