
from collections import deque
def bfs(x,y):
    queue = deque([(x,y)])
    area = 1
    graph[x][y] = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                area += 1
                graph[nx][ny] = 1
                queue.append((nx,ny))
    return area
        
        
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n,k = map(int,input().split())
graph = []
for _ in range(m):
    graph.append([0 for _ in range(n)])

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x] = 1

cnt = 0
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt+=1
            result.append(bfs(i,j))
print(cnt)
result.sort()
print(*result)