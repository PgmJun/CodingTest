from collections import deque
INF = int(1e9)
answer = INF

def checkBoundary(pos):
    if pos < 0 or pos > 100000:
        return False
    return True

def bfs():
    queue = deque([(n,0)])
    visited = [False for _ in range(100001)]

    while queue:
        pos, delay = queue.popleft()

        if pos == k:
            return delay

        if checkBoundary(pos+1) and not visited[pos+1]:
            queue.append([pos+1, delay+1])
            visited[pos+1] = True
        if checkBoundary(pos-1) and not visited[pos-1]:
            queue.append([pos-1, delay+1])
            visited[pos-1] = True
        if checkBoundary(pos*2) and not visited[pos*2]:
            queue.append([pos*2, delay+1])
            visited[pos*2] = True

    
n,k = map(int,input().split())

print(bfs())