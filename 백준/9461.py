t = int(input())
dp = [-1 for _ in range(101)]
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(t):
    n = int(input())
    if dp[n] != -1:
        print(dp[n])
    else:
        for j in range(3, n+1):
            dp[j] = dp[j-3]+dp[j-2]
        print(dp[n])
