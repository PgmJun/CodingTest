from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    count = {'k':0, 'v':0}
    count[graph[x][y]] += 1
    graph[x][y] = 'x'

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] in ['x', '#']:
                continue
            if graph[nx][ny] == '.':
                graph[nx][ny] = 'x'
                queue.append((nx,ny))
            if graph[nx][ny] in ['k','v']:
                count[graph[nx][ny]] += 1
                graph[nx][ny] = 'x'
                queue.append((nx,ny))
    
    if count['k'] > count['v']:
        resultCount['k'] += count['k']
    else:
         resultCount['v'] += count['v']



dx,dy = [-1,1,0,0],[0,0,-1,1]
n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
resultCount = {'k':0, 'v':0}
for i in range(n):
    for j in range(m):
        if graph[i][j] in ['v','k']:
            bfs(i,j)

print(resultCount['k'], resultCount['v'])
