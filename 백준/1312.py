a,b,n = map(int,input().split())

result = []
num = str(a/b)

for _ in range(1+n):
    result.append(a//b)
    a = a%b*10
print(result[-1])
