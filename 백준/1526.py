n = int(input())
arr = []
for i in range(4,n+1):
    v = str(i)
    v = v.replace('7','')
    v = v.replace('4','')
    if v == '':
        arr.append(i)

print(max(arr))