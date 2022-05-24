n = int(input())
direct = list(map(str,input().split()))

x = 1
y = 1

#방
direction = ['U','D','L','R']

#상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for d in direct:
    v = direction.index(d)
    if (x + dx[v]) < 1 or (y + dy[v]) < 1:
        continue
    else:
        x += dx[v]
        y += dy[v]
        

print('x={}, y={}'.format(y,x))
