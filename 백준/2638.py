
# 문제:
# NxM 그래프에 있는 치즈가 녹는 시간을 구해라
# 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다.

# 아이디어:
# dfs로 0,0을 시작으로 공기(0)을 찾으며 상하좌우에 치즈(1)가 있으면 그래프의 치즈 좌표값에 +1을 함
# 그리고 그리고 치즈 좌표값에 +1 한 값이 3 이상이 되면 그 자리를 0으로 변경함
# 그래프에서 치즈(1)이 없어질 때까지 time을 1 씩 증가시키며 dfs로 반복순환
# dfs 시엔 몇개의 치즈가 사라졌는지 cheese를 count 해주고 
# 사라진 cheese값이 1 이상이면 1 return 후 time에 저장, 사라진 치즈가 없다면 0 return후 return 값이 0이면 while True문 종료
# time값을 출력

from collections import deque

def bfs(x,y,graph):
    queue = deque([(x,y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    lost_cheese = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny] = True
                for i in range(4):
                    try:
                        if graph[nx+dx[i]][ny+dy[i]] > 0:
                            graph[nx+dx[i]][ny+dy[i]] += 1
                    except IndexError:
                        continue
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 2:
                    graph[i][j] = 0
                    lost_cheese += 1
            elif graph[i][j] > 0 and graph[i][j] < 3:
                graph[i][j] = 1
    return lost_cheese

# n : 세로 : m : 가로
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [0,0,-1,1],[-1,1,0,0]
time = 0

while True:
    lost_cheese = bfs(0,0,graph)
    if lost_cheese > 0:
        time += 1
    elif lost_cheese == 0:
        break

print(time)