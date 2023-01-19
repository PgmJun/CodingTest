n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(0,n):
    arr[i] = int(input())

dp = [0] * n # i번째 줄까지에서 마실 수 있는 최대 포도주 양
dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1]
    if n > 2:
        dp[2] = max(dp[1], arr[0]+arr[2], arr[1]+arr[2])
for i in range(3,n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(dp[n-1])