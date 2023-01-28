import sys
input=sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]
defIdx = []
for i in range(0, n-1):
    for c in range(len(arr[0])):
        if arr[i][c] != arr[i+1][c]:
            defIdx.append(c)

for i in range(len(arr[0])):
    if i in defIdx:
        print('?',end='')
        continue
    print(arr[0][i],end='')