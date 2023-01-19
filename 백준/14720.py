n = int(input())
milk = list(map(int,input().split()))
dp = [0] * (n+1)
now = 0

for i in range(1,n+1):
    # 안 마시고 건너뛰는 경우 / 마시는 경우
    if now == milk[i-1]:
        dp[i] = max(dp[i-1], dp[i-1]+1)
        now = (now + 1) % 3
    else:
        dp[i] = dp[i-1]

print(dp[n])