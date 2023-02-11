n = int(input())
arr = list(map(int, input().split()))
arr.reverse()  # LIS로 변경
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
