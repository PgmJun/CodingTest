#N을 K로 나누거나 N에 -1을 할 때
#N이 1이 될 때까지의 COUNT를 구하여 출력한다

import sys
input=sys.stdin.readline

n,k = map(int,input().split())
cnt = 0

while True:
    if n == 1:
        break
    
    if n%k == 0:
        cnt+=1
        n //= k
    else:
        cnt+=1
        n -= 1

print(cnt)
