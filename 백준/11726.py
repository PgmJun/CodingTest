# 점화식
# dp[i] = dp[i-1]+dp[i-2]

import sys
input=sys.stdin.readline

n = int(input())
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

if n > 4:
    for i in range(5, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 10007

print(dp[n])
