# 영식 요금제 30초에 10원
# 민식 요금제 60초에 15원
Y = 30
M = 60

n = int(input())
arr = list(map(int,input().split()))

y_sum = 0
m_sum = 0
for t in arr:
    if t == 0:
        continue
    y_sum += ((t // Y)+1) * 10
    m_sum += ((t // M)+1) * 15

if y_sum > m_sum:
    print('M', m_sum)
elif m_sum > y_sum:
    print('Y', y_sum)
else:
    print('Y M',y_sum)