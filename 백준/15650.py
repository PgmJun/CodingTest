import itertools

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

result = []
for j in itertools.combinations(arr, m):
    result.append(sorted(j))

for i in sorted(result):
    print(*i)
