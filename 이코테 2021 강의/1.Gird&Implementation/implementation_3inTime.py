# 00시 00분 00초부터 N시 00분 00초 사이의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성
# ex) 00시 00분 03초, 00시 13분 01초

n = int(input())
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(s)+str(m):
                count += 1

print(count)
