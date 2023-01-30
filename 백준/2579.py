# 가능한 이동 경우:
# 계단을 한칸 오르는 경우, 계단을 두칸 오르는 경우

# 필수 조건:
# 마지막 계단은 밟아야 함.

# 두 조건을 합쳐 생성한 조건:
# 1 2 3 4의 계단이 있다면 "1,3,4"를 고려한 경우 / "1,2,4"를 고려한 경우 (마지막 계단은 밟아야하므로 무조건 마지막은 밟는 경우 내에서 최댓값 찾기)


n = int(input())
step = [0 for _ in range(301)] # 계단은 300이하의 숫자이므로 301개의 인덱스 생성
for i in range(1,n+1):
    step[i] = int(input())

dp = [0 for _ in range(301)] # 계단은 300이하의 숫자이므로 301개의 인덱스 생성

# 기본값 주입
dp[1] = step[1]
dp[2] = step[1] + step[2]
dp[3] = max(step[1]+step[3], step[2]+step[3])
for i in range(4,n+1):
    dp[i] = max(dp[i-3]+step[i]+step[i-1], dp[i-2]+step[i])

print(dp[n])