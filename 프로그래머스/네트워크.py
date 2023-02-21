def dfs(start, visited, graph):
    visited[start] = True
    for v in graph[start]:
        if visited[v]:
            continue
        if not visited[v]:
            dfs(v, visited, graph)
    return


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n

    # computers를 연결관계 graph로 변경
    j = -1
    for c in computers:
        j += 1
        for i in range(len(c)):
            if c[i] == 1 and i != j:
                graph[j].append(i)

    # 0부터 n-1번까지 탐색
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, visited, graph)

    return answer
