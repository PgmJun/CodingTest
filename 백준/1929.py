import sys
input = sys.stdin.readline


def findSosu(m, n):
    check = [True] * (n+1)
    check[0], check[1] = False, False

    for i in range(2, int(n**(1/2))+1):
        for j in range(i*i, n+1, i):
            if check[j] == True:
                check[j] = False

    for i in range(m, n+1):
        if check[i]:
            print(i)


m, n = map(int, input().split())
findSosu(m, n)
