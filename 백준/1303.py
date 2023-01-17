from collections import deque

def bfs(x,y,type):
    queue = deque([(x,y)])
    cnt = 1
    graph[x][y] = 'x'

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx,ny = a+dx[i], b+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != type:
                continue
            if graph[nx][ny] == type:
                cnt += 1
                graph[nx][ny] = 'x'
                queue.append((nx,ny))
    return cnt

dx, dy = [-1,1,0,0], [0,0,-1,1]

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))

wpower, bpower = 0, 0

for i in range(n):
    for j in range(m):
        if graph[j][i] == 'B':
            bcnt = bfs(j,i,'B')
            bpower += (bcnt ** 2)
        elif graph[j][i] == 'W':
            wcnt = bfs(j,i,'W')
            wpower += (wcnt ** 2)

print(wpower, bpower)