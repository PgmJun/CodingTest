import itertools

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

result = []
for j in itertools.combinations_with_replacement(arr, m):
    result.append(j)

for i in sorted(result):
    print(*i)
