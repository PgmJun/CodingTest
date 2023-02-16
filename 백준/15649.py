import itertools

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)
print(arr)

result = []
for j in itertools.permutations(arr, m):
    result.append(j)

for i in sorted(result):
    print(*i)
