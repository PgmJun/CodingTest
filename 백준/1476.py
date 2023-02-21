import sys
input = sys.stdin.readline

e,s,m = map(int,input().split())
# 15 28 19
a,b,c = 1,1,1
year = 1
while True:
    if a == e and b == s and c == m:
        print(year)
        break
    year += 1
    a += 1
    b += 1
    c += 1
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1