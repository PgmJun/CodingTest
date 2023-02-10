import sys
input = sys.stdin.readline
# (0,r-1) -> (c-1,0) 까지 k번만에 가는 경우의 수 탐색
# dfs 사용
def bfs():


graph = []
r, c, k = map(int, input().rstrip().split())

for _ in range(r):
    graph.append(input().rstrip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
print(graph)
