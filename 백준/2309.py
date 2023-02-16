import itertools

arr = []
for _ in range(9):
    arr.append(int(input()))
result = []

for i in itertools.combinations(arr,7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break