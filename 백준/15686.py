import itertools
import sys
input = sys.stdin.readline
# 그래프에서 1의 좌표(homeArr), 2의 좌표(chicArr) 저장
# 치킨집 별로 각 집들에 대한 치킨거리를 구하여 chicLength 배열에 저장
#
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


homeArr = []
chicArr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        elif graph[i][j] == 1:
            homeArr.append([i, j])
        elif graph[i][j] == 2:
            chicArr.append([i, j])

chicLength = [[] for _ in range(len(chicArr))]
for i in range(len(chicArr)):
    for hx, hy in homeArr:
        chicLength[i].append(abs(chicArr[i][0]-hx) + abs(chicArr[i][1]-hy))

result = 1e9
# chicLength에 저장되는 치킨거리와 C에서 출력되는 치킨거리가 다름
for c in itertools.combinations(chicLength, m):
    print(c)
    for i in range(len(homeArr)):
        for j in range(1, m):
            c[0][i] = min(c[0][i], c[j][i])
    result = min(result, sum(c[0]))

print(result)
