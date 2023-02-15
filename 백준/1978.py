n = int(input())
arr = list(map(int,input().split()))
result = 0
for v in arr:
    if v == 1:
        continue
    cnt = 0
    for i in range(2,v):
        if cnt > 1:
            break
        if v % i == 0:
            cnt += 1
    if cnt == 0:
        result+=1

print(result)