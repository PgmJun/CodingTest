n = int(input())
dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for _ in range(n):
    t = int(input())

    for i in range(1, t+1):
        if dp[i] != 0:
            continue
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    
    print(dp[t])