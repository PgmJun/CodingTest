arr = []
for _ in range(int(input())):
    arr.append(list(input().split()))

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for a in arr:
    print(a[0])