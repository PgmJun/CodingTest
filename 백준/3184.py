from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    oCnt, vCnt = 0,0
    if graph[x][y] == 'v': # 늑대일 때 카운트
        vCnt+=1
    elif graph[x][y] == 'o': # 양일 때 카운트
        oCnt+=1
    graph[x][y] = '#' # 카운트한 곳은 다시 탐색하지 않도록 울타리('#')로 변경
    while queue:
        x,y = queue.popleft()
        for i in range(4): # 연결되어있는 상하좌우 탐색
            nx,ny = x+dx[i],y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위가 0보다 작거나 범위보다 클때 생략
                continue
            if graph[nx][ny] == '#': # 좌표의 위치가 울타리('#')면 생략
                continue
            if graph[nx][ny] in ['.','o','v']: # 좌표의 위치가 '.','o','v' 중 하나일 때 queue에 추가
                queue.append((nx,ny))
                if graph[nx][ny] == 'o': # 좌표의 위치가 양일 때 카운트
                    oCnt +=1
                elif graph[nx][ny] == 'v': # 좌표의 위치가 늑대일 때 카운트
                    vCnt += 1
                graph[nx][ny] = '#' # 카운트한 곳은 다시 탐색하지 않도록 울타리('#')로 변경
    if oCnt > vCnt: # 계산이 끝난 후 양이 늑대보다 많으면 살아남은 양의 수를 return
        return ['o',oCnt]
    elif vCnt >= oCnt: # 계산이 끝난 후 늑대가 양보다 많거나 같으면 살아남은 늑대의 수를 return
        return ['v',vCnt]

dx,dy = [-1,1,0,0],[0,0,-1,1]
r,c = map(int,input().split())
result = {'o':0, 'v':0} # 양과 늑대의 수를 저장하기 위한 dict
graph = [list(input()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v' or graph[i][j] == 'o':
            v = bfs(i,j)
            result[v[0]] += v[1] # 탐색 결과 반영

print(result['o'], result['v']) # 살아남은 양의 수와 살아남은 늑대의 수 출력