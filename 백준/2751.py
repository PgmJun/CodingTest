import sys
input = sys.stdin.readline

n = int(input().rstrip())
nlist = []
for _ in range(n):
    nlist.append(int(input().rstrip()))
    
nlist.sort()
for n in nlist:
    print(n)
