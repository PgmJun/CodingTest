from collections import deque
import copy 
import sys
input=sys.stdin.readline


def minusOne(x,y): 
    minusResult = copy.deepcopy(graph[x][y]) # 원본 그래프의 특정 좌표의 빙산 높이를 복사
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0: # 상하좌우에 0이 있을 때
            if minusResult > 0: # 빙산 높이가 0보다 크면 -1
                minusResult -= 1

    return minusResult

def bfs_checkCount(x,y, graph):
    queue = deque([(x,y)])
    graph[x][y] = 0
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx,ny = a+dx[i],b+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] > 0:
                graph[nx][ny] = 0
                queue.append((nx,ny))

dx,dy = [-1,1,0,0], [0,0,-1,1]
cnt = 1
year = 0
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

copyGraph = copy.deepcopy(graph) # 그래프를 복사하여 변경을 적용할 그래프를 생성
while cnt < 2:
    year += 1 # try 횟수 카운트

    # 0,0 부터 n-1,m-1까지 전부 돌며 각 좌표에 상하좌우 0의 갯수만큼 -1한 값 minusResult를 그래프의 각 좌표에 저장함
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                minusResult = minusOne(i,j)
                copyGraph[i][j] = minusResult # 카피 그래프에 변경사항 반영

    tempCnt = 0 # 빙산의 갯수
    graph = copy.deepcopy(copyGraph) # 카피 그래프를 통해 빙산의 갯수를 측정할 것이므로 원본 그래프에 변경사항을 반영
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] > 0: # 카피 그래프에 bfs를 적용하여 빙산의 갯수를 측정 (특정 좌표의 값이 0보다 크다면 빙산 갯수를 카운트하고, 연결된 빙산의 값을 0으로 변경)
                bfs_checkCount(i,j,copyGraph)
                tempCnt += 1
    # 모든 빙산의 갯수가 0이면 0을 출력하도록 year을 0으로 변경하고 반복문을 종료한다.
    if tempCnt == 0: 
        year = 0
        break
    # 빙산의 갯수가 0보다 크면 cnt에 빙산의 갯수를 저장
    else:
        cnt = tempCnt
# 총 걸린 년수 출력
print(year)