# 첫 반복문으로 knowTrueList에 있는 사람이 있는 파티에 참여하는 사람을 모두 knowTrueList에 추가, graph에 append (1차 필터링)
# 두번째 반복문으로 knowTrueList에 있는 사람이 참여하지 않는 파티면 COUNT (knowTrueList 사용하여 2차 필터링)
# COUNT한 변수 출력

# 변수
# n: 사람 수 | m: 파티 수 | knowTrueList: 진실을 아는 사람 번호| partyList: 파티 참석 List | people: 1개의 파티에 참석하는 사람 List | result: 과장된 이야기를 할 수 있는 파티의 수 | cnt: 과장해서 얘기가 가능한 파티 수
# -*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline  # \n 까지 받아옴
def MIS(): return map(int, input().rstrip().split())


n, m = MIS()
_, *knowTrueList = MIS()
knowTrueList = set(knowTrueList)

partyList = [set(list(MIS())[1:]) for _ in range(m)]

for _ in range(m):
    for people in partyList:
        if knowTrueList & people:
            knowTrueList |= people


res = 0
for party in partyList:
    if not (party & knowTrueList):
        res += 1

print(res)
