from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    graph[x][y] = '0'
    cnt = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx,ny = a+dx[i],b+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == '0':
                continue
            if graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                cnt+=1
                queue.append((nx,ny))
    return cnt


dx,dy = [-1,1,0,0],[0,0,-1,1]
n = int(input())
vcnt = 0
result = []
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            vcnt += 1
            result.append(bfs(i,j))
result.sort()
print(vcnt)
for v in result:
    print(v)