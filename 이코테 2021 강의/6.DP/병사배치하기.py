n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
# 4 2 5 8 4 11 15
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
