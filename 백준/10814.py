n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().split()))

arr.sort(key=lambda x: (int(x[0])))

for a,n in arr:
    print(a,n)