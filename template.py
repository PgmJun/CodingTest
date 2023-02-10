# -*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline  # \n 까지 받아옴
def MIS(): return map(int, input().rstrip().split())  # rstrip() -> \n 제거

# MIS 템플릿 사용법
# n, m = MIS()
# graph = [list(input().rstrip()) for _ in range(n)]

# print(n, m)
# print(graph)


# # defaultdict - (int)형 value를 갖는 dict생성 -> 모든 키에 대해 default값이 0
# mdict = defaultdict(int)
# mdict['a'] += 10
# print(mdict['a'])
