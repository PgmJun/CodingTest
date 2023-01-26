# 3, 5kg의 설탕봉지로 정확히 NKg의 설탕을 옮기는 가장 최소한의 봉지 수
# Nkg을 만들 수 없다면 -1 출력 
# 3 <= n <= 5000
# dp[i] : ikg을 옮기는 최소 봉지 수

n = int(input())
dp = [-1] * (n+1)

dp[0] = -1
dp[1] = -1
dp[2] = -1
dp[3] = 1
if n > 3:
    dp[4] = -1
    if n > 4:
        dp[5] = 1
        if n > 5:
            for i in range(6,n+1):
                if dp[i-3] == -1 and dp[i-5] == -1:
                    continue
                if dp[i-3] != -1 and dp[i-5] != -1:
                    dp[i] = min(dp[i-3]+1, dp[i-5]+1)
                elif dp[i-3] != -1 and dp[i-5] == -1:
                    dp[i] = dp[i-3]+1
                elif dp[i-3] == -1 and dp[i-5] != -1:
                    dp[i] = dp[i-5]+1

print(dp[n])
