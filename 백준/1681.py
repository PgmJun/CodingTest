n,l = map(int,input().split())
arr = []
for i in range(1,int(1e9)):
    if len(arr) == n :
        break
    if str(l) in str(i):
        continue
    arr.append(i)

print(arr[-1])