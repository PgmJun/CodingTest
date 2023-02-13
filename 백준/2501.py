n, k = map(int, input().split())
arr = [1]

for i in range(2, n+1):
    if n % i == 0:
        arr.append(i)

try:
    print(arr[k-1])
except IndexError:
    print(0)
