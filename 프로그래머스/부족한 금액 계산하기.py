# 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배
# 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상

# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return
# 단, 금액이 부족하지 않으면 0을 return

# price: 놀이기구 이용료
# money: 처음 가진 금액
# count: 놀이기구 이용 횟수

def solution(price, money, count):
    answer = -1

    for c in range(1, count+1):
        money -= (price * c)

    if money < 0:
        answer = abs(money)
    else:
        answer = 0

    return answer
