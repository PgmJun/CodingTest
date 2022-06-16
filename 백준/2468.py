#2차원 배열 깊은 복사(deep copy)에 필요한 부품
import copy

#런타임 에러 방지
import sys 
sys.setrecursionlimit(100000)
r = sys.stdin.readline

def dfs(x,y,h):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if tmpGraph[x][y] > h:
        tmpGraph[x][y] = -1
        dfs(x-1,y,h)
        dfs(x,y-1,h)
        dfs(x+1,y,h)
        dfs(x,y+1,h)
        return True
    return False

maxvalue = -1
n = int(r())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in graph[i]:
        if j > maxvalue:
            maxvalue = j
        
result = []
for k in range(maxvalue):
    cnt = 0
    tmpGraph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if dfs(i,j,k) == True:
                cnt+=1
    result.append(cnt)

print(max(result))
