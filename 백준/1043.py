# knowTrueList에 있는 사람이 파티에 참석하면 그 파티에 있는 사람 전부 knowTrueList에 추가 및 knowTrueList에 있는 사람이 참여하는 파티 graph에서 제거
# len(graph) 출력으로 정답 확인
# 변수
# n: 사람 수 | m: 파티 수 | knowTrueList: 진실을 아는 사람 번호 | result: 과장된 이야기를 할 수 있는 파티의 수 | graph: 파티에 참석하는 사람 데이터
import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())
knowTrueList = list(map(int, input().rstrip().split()))
del knowTrueList[0]
knowTrueList = set(knowTrueList)
print(knowTrueList)

for _ in range(m):
    a = list(map(int, input().rstrip().split()))
    del a[0]
    a = set(a)
    knowTrueList &= a

for _ in range(m):
