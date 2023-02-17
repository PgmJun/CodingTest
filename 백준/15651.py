import itertools

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

result = []
for j in itertools.product(arr, repeat=m):
    result.append(j)

for i in sorted(result):
    print(*i)
