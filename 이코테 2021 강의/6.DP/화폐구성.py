INF = 10001
n, m = map(int, input().split())
amount = []

for _ in range(n):
    amount.append(int(input()))

# dp[i] : i원을 만들기 위한 최소 화폐 갯수
dp = [INF] * (m+1)
# 0원을 만들기 위한 화폐 갯수 0개
dp[0] = 0

for a in amount:
    for j in range(a, m+1):
        if dp[j - a] != INF:  # (j-a)원을 만드는 방법이 존재한다면
            dp[j] = min(dp[j], dp[j-a]+1)

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])
