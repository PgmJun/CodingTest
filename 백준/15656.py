from itertools import product

n,m = map(int,input().split())
arr = list(map(int,input().split()))

result = []

for i in product(arr,repeat=m):
    result.append(i)

for r in sorted(result):
    print(*r)