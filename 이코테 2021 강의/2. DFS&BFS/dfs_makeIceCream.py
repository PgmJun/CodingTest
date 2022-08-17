# 음료수 얼려먹기 알고리즘 문제
# N x M 크기의 얼음 틀이 있다. 구멍이 뚫린 부분은 0, 칸막이는 1로 표시된다.
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성해라.

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
