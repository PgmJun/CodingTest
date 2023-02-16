n = int(input())
arr1 = set(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))

for v in arr2:
    if v in arr1:
        print(1,end=' ')
    elif v not in arr1:
        print(0,end=' ')
print()