# 곱하기 혹은 더하기 알고리즘 문제
# 02984 와 유사한 형태로 문자열 S가 주어지면 왼쪽부터 차례대로 더하거나 곱하여 나올 수 있는 가장 큰 값을 산출하는 문제


s = input()
result = int(s[0])

for i in range(1, len(s)):
    print(result)
    if result <= 1:
        result += int(s[i])
    elif result > 1:
        result *= int(s[i])

print(result)
