from collections import deque


def bfs(findList):
    queue = deque(findList)
    # graph[nx][ny]이 0인 좌표를 찾아 이전값인 graph[x][y]에 +1한 값을 graph[nx][ny]에 설정
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx, ny])


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
findList = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            findList.append([i, j])

bfs(findList)

# 그래프에서 가장 큰 값을 탐색하여 토마토가 익을 때 까지 걸린 (최소날짜+1) 값을 찾는다
# 만약 탐색이 끝난 후에도 그래프에 익지 못한 토마토(0)이 남아있으면 -1을 출력하도록 0을 return
result = 0
for g in graph:
    if 0 in g:
        result = 0
        break
    result = max(max(g), result)
# 1부터 시작하여 result까지 증가하였기에 소요된 일수를 구하려면 -1을 해주어야한다.
print(result-1)
