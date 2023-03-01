import heapq
x = int(input())
sticks = [64]

while True:
    if sum(sticks) <= x:
        break
    scm = heapq.heappop(sticks)
    halfScm = scm // 2
    
    if halfScm + sum(sticks) >= x:
        heapq.heappush(sticks, halfScm)
    else:
        heapq.heappush(sticks, halfScm)
        heapq.heappush(sticks, halfScm)

print(len(sticks))