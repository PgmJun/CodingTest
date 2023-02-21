import itertools

n = int(input())
arr = list(map(int,input().split()))
max = -1e9

for a in itertools.permutations(arr,len(arr)):
    sum = 0
    for i in range(len(a)-1):
        sum += abs(a[i]-a[i+1])
    if sum > max:
        max = sum

print(max)
