import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = []
for _ in range(n):
    a,b = map(int,input().rstrip().split())
    result.append([a,b])
result.sort()
for data in result:
    print('{} {}'.format(data[0],data[1]))