# 확률과 통계 순열 nCr(Combination) 문제
# 1010-1처럼 combinations 사용해서 풀면 combinations가 무거운 함수라서 메모리 초과뜸

import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    a = math.factorial(m)
    b = math.factorial(m-n)*math.factorial(n)
    print(int(a/b))
