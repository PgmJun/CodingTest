from itertools import combinations #콤비네이션이 무거워서 메모리 초과 뜸
import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().rstrip().split())
    data = list(combinations(range(1, m+1), n))
    print(len(data))
