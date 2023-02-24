from collections import deque


def bfs(x, y, d):
    queue = deque([(x, y)])
    cnt = 0

    while queue:
        x, y = queue.popleft()
        # 현재 청소되지 않은 경우 청소
        if graph[x][y] == 0:
            graph[x][y] = -1
            cnt += 1
        # 주변 4칸 탐색
        NearNoneCleanArea = False
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if graph[nx][ny] == 0:
                NearNoneCleanArea = True
                break

        # 주변 4칸에 청소되지 않은 빈칸이 없는 경우
        if not NearNoneCleanArea:
            # 방향을 전환하지 않고 후진하는데
            if graph[x+dx[(d+2) % 4]][y+dy[(d+2) % 4]] == 1:  # 뒷칸이 벽이면 작동 중지
                queue.clear()
                break
            # 청소안된 또는 청소된 구역이면 뒤로 이동
            elif graph[x+dx[(d+2) % 4]][y+dy[(d+2) % 4]] in [-1, 0]:
                queue.append([x+dx[(d+2) % 4], y+dy[(d+2) % 4]])
        # 주변 4칸에 청소되지 않은 빈칸이 있는 경우
        elif NearNoneCleanArea:
            # 반시계 방향으로 90도 회전
            d = (d+3) % 4
            # 해당 방향이 청소되어있지 않으면 전진
            if graph[x+dx[d]][y+dy[d]] == 0:
                queue.append([x+dx[d], y+dy[d]])
            # 그렇지 않으면 이동하지 않음
            else:
                queue.append([x, y])  # (이 부분 빼먹지 않도록 주의)

    return cnt


n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 0: 청소되지 않은 | -1: 청소된 | 1: 벽
graph = [list(map(int, input().split())) for _ in range(n)]

# 0:북 | 1:동 | 2:남 | 3:서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

print(bfs(x, y, d))
