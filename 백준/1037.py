# 특정 수 a에 대한 약수를 모두 제공받는다
# 약수의 갯수는 n개이며 이를 통해 특정 수 a를 구해야한다.
# 모든 약수를 제공받기 때문에 약수 중 (가장 작은 수 * 가장 큰 수)를 곱하면 정답이 나올 것이다.

n = int(input())
arr = list(map(int, input().split()))

print(min(arr) * max(arr))
