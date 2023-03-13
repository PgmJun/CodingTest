from collections import deque
from copy import deepcopy

MAX_WIDTH, MAX_HEIGHT = 3, 4


def bfs(pos, find, graph):
    queue = deque([pos])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    visited = [[False for _ in range(MAX_WIDTH)] for _ in range(MAX_HEIGHT)]
    visited[pos[0]][pos[1]] = True

    while queue:
        p = queue.popleft()

        if graph[p[0]][p[1]] == find:
            pos = [p[0], p[1], p[2]]
            break

        for i in range(4):
            nx, ny = p[0] + dx[i], p[1] + dy[i]

            if nx < 0 or nx >= MAX_HEIGHT or ny < 0 or ny >= MAX_WIDTH:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append([nx, ny, p[2]+1])

    return pos


def solution(numbers, hand):
    answer = ''
    graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    p_d_left, p_d_right = [3, 0, 0], [3, 2, 0]

    for n in numbers:

        if n in [1, 4, 7]:
            p_d_left = bfs(p_d_left, n, graph)
            answer += 'L'

        elif n in [3, 6, 9]:
            p_d_right = bfs(p_d_right, n, graph)
            answer += 'R'

        else:
            p_d_left_result = bfs(p_d_left, n, graph)
            p_d_right_result = bfs(p_d_right, n, graph)

            if p_d_left_result[2] < p_d_right_result[2]:
                p_d_left = p_d_left_result
                answer += 'L'

            elif p_d_left_result[2] > p_d_right_result[2]:
                p_d_right = p_d_left_result
                answer += 'R'

            else:
                answer += hand.upper()[0]
                if hand == 'left':
                    p_d_left = p_d_left_result
                elif hand == 'right':
                    p_d_right = p_d_left_result

        p_d_left[2], p_d_right[2] = 0, 0

    return answer
