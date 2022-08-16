# 1이 될 때까지 알고리즘 문제
# N,K과 선택지 2개가 주어진다.
# 1. N을 -1 한다. | 2. N을 K로 나눈다.
# N이 1이 될 떄까지 1번 혹은 2번 과정을 수행해야하는 횟수를 구하는 것이 문제이다.

n, k = map(int, input().split())
result = 0

while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    result += 1

print(result)
