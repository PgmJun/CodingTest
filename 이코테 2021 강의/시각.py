# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세

n = int(input())
find = 3 #찾는 수
cnt = 0 # 시간에 FIND가 있는 경우의 수
min_cnt = 0 #00분00초~59분59초 사이에 FIND가 있는 경우의 수


#시간에 FIND가 포함되지 않은 경우,
#00분00초~59분59초 사이에 FIND가 있는 경우의 수를 더해줌
for i in range(60):
    for k in range(60):
        if str(find) in str(i)+str(k):
            min_cnt+=1

for hour in range(n+1):
    if str(find) in str(hour):
        cnt += 60**2 #00분00초 ~ 59분59초까지의 경우의 수
        continue
    else:
        cnt += min_cnt
        
print(cnt)
