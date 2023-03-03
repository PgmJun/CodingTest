# arr[0] : 키가 1인 사람이 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있는지에 대한 값
 
# 왼쪽에 0의 갯수가 arr[i]개 이며, 현재 인덱스의 값이 0이면 현재 인덱스의 값을 i+1로 설정

n = int(input())
arr = list(map(int,input().split()))
result = [0 for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(len(result)):
        if cnt == arr[i]:
            if result[j] != 0:
                continue
            result[j] = i+1
            break
        if result[j] == 0:
            cnt+=1
    
print(*result)