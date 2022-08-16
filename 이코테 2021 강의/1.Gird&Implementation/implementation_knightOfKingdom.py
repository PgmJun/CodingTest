loc = input()
locX = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
locY = ['1', '2', '3', '4', '5', '6', '7', '8']

count = 0

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

x = locX.index(loc[0])
y = locY.index(loc[1])

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    count += 1
print(count)
