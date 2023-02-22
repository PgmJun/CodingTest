# 분류 : BFS

from collections import deque


def bfs(x, y, graph):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(x, y)])
    MAP_WIDTH = len(graph[0])
    MAP_HEIGHT = len(graph)

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if nx < 0 or nx >= MAP_HEIGHT or ny < 0 or ny >= MAP_WIDTH:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx, ny])

    if graph[MAP_HEIGHT-1][MAP_WIDTH-1] == 1:
        return -1
    else:
        return graph[MAP_HEIGHT-1][MAP_WIDTH-1]


def solution(maps):
    answer = bfs(0, 0, maps)

    return answer
