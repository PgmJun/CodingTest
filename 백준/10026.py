# RGB 로 이루어진 그래프가 주어짐
# 적록 색약을 가진 사람이은 R과 G를 같은 것으로 봄

# 문제: 주어진 그래프에서 적록 색약이 보는 구역과 일반인이 보는 구역 갯수 출력
# 아이디어:
# graph를 deepcopy 해서 정상인용과 색약인용 그래프 2개 생성
import copy,sys
sys.setrecursionlimit(int(1e9))


def dfs(x,y,color,graph):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if graph[x][y] != color:
        return
    if graph[x][y] == color:
        graph[x][y] = 'X'
        dfs(x+1, y, color, graph)
        dfs(x-1, y, color, graph)
        dfs(x, y+1, color, graph)
        dfs(x, y-1, color, graph)
        



n = int(input())
cntDict = {'nmCnt':0, 'cwCnt':0}

nmGraph = [list(input()) for _ in range(n)]
cwGraph = copy.deepcopy(nmGraph)

# 색약 그래프 생성
for i in range(n):
    for j in range(n):
        if cwGraph[i][j] in ['R','G']:
            cwGraph[i][j] = 'RG'

# dfs로 계산
for i in range(n):
    for j in range(n):
        if nmGraph[i][j] in ['R','G','B']:
            cntDict['nmCnt'] += 1
            dfs(i,j,str(nmGraph[i][j]), nmGraph)
        if cwGraph[i][j] in ['RG','B']:
            cntDict['cwCnt'] += 1
            dfs(i,j,str(cwGraph[i][j]), cwGraph)

print(cntDict['nmCnt'], cntDict['cwCnt'])