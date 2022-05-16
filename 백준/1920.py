import sys
input=sys.stdin.readline

n = int(input())
a = set(map(int,input().split()))
m = int(input())
M = list(map(int,input().split()))

for i in range(len(M)):
    if M[i] in a:
        print(1)
    else:
        print(0)
