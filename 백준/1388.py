from collections import deque
def bfs(x,y,floorType):
    queue = deque([(x,y)])
    graph[x][y] = 'x'
    while queue:
        x,y = queue.popleft()
        for i in range(2):
            if floorType == '|':
                nx,ny = x+dx[i], y
            elif floorType == '-':
                nx,ny = x, y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 'x':
                continue
            if graph[nx][ny] == floorType:
                queue.append([nx,ny])
                graph[nx][ny] = 'x'


dx,dy = [-1,1],[-1,1]

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 'x':
            result += 1
            bfs(i,j,graph[i][j])

print(result)