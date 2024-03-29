'''
input)
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

output)
19
16
'''

for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i+1][j-1])
            elif i == n-1:
                dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i-1][j-1])
            elif i not in [0, n-1]:
                dp[i][j] = dp[i][j] + \
                    max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1])
    result = 0
    for d in dp:
        result = max(result, max(d))
    print(result)
