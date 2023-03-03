from collections import deque

def bfs(num, goal):
    result = -1
    queue = deque([(num,1)])

    while queue:
        n,c = queue.popleft()
        if n > goal:
            continue
        if n == goal:
            result = c
            break
        queue.append([n*2,c+1])
        queue.append([n*10+1,c+1])
    
    return result



a,b = map(int,input().split())
print(bfs(a,b))
