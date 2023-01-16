from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    cnt = 1
    graph[x][y] = '.'
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx,ny = a+dx[i],b+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '.':
                continue
            if graph[nx][ny] == '#':
                cnt+=1
                queue.append((nx,ny))
                graph[nx][ny] = '.'
    return cnt


dx = [-1,1,0,0]
dy = [0,0,-1,1]

max = -1
n,m,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(['.' for _ in range(m)])

for i in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1] = '#'

for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            v = bfs(i,j)
            if v > max:
                max = v

print(max)