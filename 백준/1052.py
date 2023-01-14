# 피보나치 함수에서 0과 1이 출력되는 횟수 구하기
#
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    zero_cnt = [1, 0]
    one_cnt = [0, 1]
    for i in range(1, n):
        zero_cnt.append(zero_cnt[i-1] + zero_cnt[i])
        one_cnt.append(one_cnt[i-1] + one_cnt[i])
    print(zero_cnt[n], one_cnt[n])
