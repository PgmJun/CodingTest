# left_cnt, right_cnt 변수 생성후       '('=left_cnt+=1   ,  ')'=right_cnt-=1
# 문자열의 모든 문자의 수를 체크했다면 result 변수에 left_cnt와 right_cnt 의 합을 저장
# 만약 result가 0이면 'YES', 0이 아니면 'NO' 출력
# (와 )의 개수가 다를 수 없기 때문
# 로직이 끝나기 전 left_cnt, right_cnt의 합이 -1 이 되면 )()( 와 같은 경우이므로 바로 NO 출력
import sys
input = sys.stdin.readline


def checkPs(psData):
    left_cnt = 0
    right_cnt = 0
    for i in range(len(psData)):
        if psData[i] == '(':
            left_cnt += 1
        elif psData[i] == ')':
            right_cnt -= 1
        if left_cnt + right_cnt < 0:
            break

    result = left_cnt + right_cnt
    if result == 0:
        print('YES')
    elif result != 0:
        print('NO')


n = int(input().rstrip())
for _ in range(n):
    checkPs(list(input().rstrip()))
