from collections import deque

n,m = map(int,input().split())
queue = deque([i for i in range(1,n+1)])
findArr = list(map(int,input().split()))

cnt = 0
for f in findArr:
    idx = queue.index(f)
    if idx == 0:
        queue.popleft()
        continue
    if 0 < idx <= len(queue)//2:
        queue.rotate(-idx)
        cnt+=idx
    elif len(queue)//2 < idx:
        queue.rotate(len(queue) - idx)
        cnt+= (len(queue) - idx)
    queue.popleft()

print(cnt)