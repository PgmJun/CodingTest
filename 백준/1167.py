# HINT : 가장 먼 트리 중 하나는 임의의 노드에서 가장 먼 노드이다.
# 그렇게 구해진 하나의 노드에서 가장 멀리있는 노드를 하나 구하면 결과를 얻을 수 있다.

from collections import deque
import sys

input = sys.stdin.readline 

def bfs(startNode, graph):
    visited = [False] * (n+1)
    queue = deque([startNode])
    visited[startNode] = True
    distanceArr = [0 for _ in range(n+1)]

    while queue:
        node = queue.popleft()
        for to, distance in graph[node]:
            if visited[to]:
                continue

            distanceArr[to] = distanceArr[node] + distance
            visited[to] = True
            queue.append(to)

    return [distanceArr.index(max(distanceArr)), max(distanceArr)]


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    nodeArr = list(map(int,input().split()))
    nodeArr.remove(-1)

    for i in range(1,len(nodeArr),2):
        graph[nodeArr[0]].append((nodeArr[i],nodeArr[i+1]))
    

longDistanceNode1 = bfs(1,graph)
longDistanceNode2 = bfs(longDistanceNode1[0],graph)

print(longDistanceNode2[1])