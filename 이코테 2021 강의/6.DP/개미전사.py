n = int(input())
arr = list(map(int,input().split()))

dp = [0] * 100

#dp
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2,n):
    # 식량창고 i-1까지에서 최고값과 식량창고 i-2까지에서의 최고값 + 창고 i에 있는 값을 비교
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    print(dp)
print(dp)
print(dp[n-1])
