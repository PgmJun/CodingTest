arr = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if arr[i][j] == 'F':
                cnt += 1
    if i % 2 == 1:
        for j in range(1, 8, 2):
            if arr[i][j] == 'F':
                cnt += 1

print(cnt)
