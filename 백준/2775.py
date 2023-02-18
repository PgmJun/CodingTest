MAX_HO = 15
MAX_FLOOR = 15

dp = [[0 for _ in range(MAX_HO)] for _ in range(MAX_FLOOR)]
dp[0] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    for i in range(1,k+1):
        for j in range(1,MAX_HO):
            if dp[i][j] != 0:
                continue
            elif dp[i][j] == 0:
                dp[i][j] = sum(dp[i-1][1:j+1])
    print(dp[k][n])
