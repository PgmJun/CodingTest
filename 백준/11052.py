# dp[i] : i개의 카드를 사는데 필요한 최댓값
n = int(input())
money = [0] + list(map(int,input().split()))

dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(0,i):
        dp[i] = max(money[i], dp[i-j]+money[j], dp[i])
    
print(dp[n])