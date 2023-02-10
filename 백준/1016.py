a, b = map(int, input().split())
cnt = 0
dp = [-1 for _ in range(b-a+1)]  # dp[i] : i의 제곱
for x in range(a, b+1):
    zegopnono = True
    for i in range(2, x):
        if dp[i] == -1:
            dp[i] = i**2
        if x % dp[i] == 0:
            zegopnono = False
            break
    if zegopnono:
        cnt += 1
print(cnt)
