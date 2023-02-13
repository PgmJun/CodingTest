from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

for i in range(int(input())):
    order = input().split()
    if order[0] == 'push_back':
        queue.append(order[1])
    elif order[0] == 'push_front':
        queue.appendleft(order[1])
    elif order[0] == 'pop_front':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop_back':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif order[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    elif order[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
