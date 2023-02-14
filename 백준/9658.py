n = int(input())
dp = [0 for _ in range(1001)]
# dp[i] = 돌 i개 로 완벽하게 게임했을때 돌을 잡은 사람
dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'
dp[4] = 'CY'

for i in range(5,n+1):
    if dp[i-1] == 'CY' and dp[i-3] == 'CY' and dp[i-4] == 'CY':
        dp[i] = 'SK'
    else:
        dp[i] = 'CY'
if dp[n] == 'CY':
    print('SK')
else:
    print('CY')