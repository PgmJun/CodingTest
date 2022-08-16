# N x N 2차원 공간이 생성됩니다.
# 공간은 (1,1) ~ (5,5) 로 존재합니다.
# 왼쪽 오른쪽 위 아래를 LRUD로 입력받아 최종적으로 도착할 지점의 좌표를 x y 형태로 출력해라
# 공간 밖으로 나가는 움직임은 skip 한다.

n = int(input())
d_list = list(input().split())
# 시작 좌표
x, y = 1, 1

move_type = ['L', 'R', 'U', 'D']

# L R U D 순서
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for d in d_list:
    for i in range(len(move_type)):
        if d == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
