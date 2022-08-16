# 거스름 돈 문제
# 거스름 돈을 500 , 100 , 50 , 10 원으로 줄 때 각 동전의 갯수

money_list = [500, 100, 50, 10]

change = int(input())
result = [0, 0, 0, 0]

for i in range(len(money_list)):
    result[i] = (change // money_list[i])
    change %= money_list[i]

for i in range(len(result)):
    print(money_list[i], ' = ', result[i], '개')
