# 모험가 길드 알고리즘 문제
# N명의 모험가를 대상으로 공포도 X를 입력 받는다
# 공포도가 X인 모험가는 X명 이상으로 구성된 모험가 그룹에 참가해야 한다.
# N명의 모험가에 대한 정보가 주어졌을 때 여행을 떠날 수 있는 그룹 수의 최댓값을 구해라

n = int(input())
x = list(map(int, input().split()))
x.sort()

count = 0
result = 0

for i in x:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
