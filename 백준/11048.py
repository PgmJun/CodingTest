n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            dp[i][j] = graph[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        elif i == 0 and j > 0:
            dp[i][j] = graph[i][j] + dp[i][j-1]
        elif i > 0 and j == 0:
            dp[i][j] = graph[i][j] + dp[i-1][j]
        elif i == 0 and j == 0:
            dp[i][j] = graph[0][0]

print(dp[n-1][m-1])