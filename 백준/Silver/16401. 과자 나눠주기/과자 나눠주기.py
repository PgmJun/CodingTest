import sys
input = sys.stdin.readline

m,n = map(int, input().split())
lenArr = list(map(int, input().split()))

start = 1 #과자 길이가 1 이상이기 때문에 start = 1로 시작
end = int(1e9)

ans = 0
while start <= end:
    # mid: 이 과자길이로 나눠주면 어떨까에 대한 값
    mid = (end + start) // 2
    
    # c: mid사이즈로 모든 과자들을 나누었을 떄 나오는 과자 갯수
    c = 0
    for l in lenArr:
        c += l // mid

    # mid사이즈로 만들어진 과자갯수c가 조카들의 수m보다 많거나 같으면
    # 현재 답과 mid를 비교하여 더 큰 값을 답으로 정하고
    # mid 보다 더 큰 크기로 과자를 나누어줄 수 있는지 탐색한다.
    if c >= m:
        ans = max(ans, mid)
        start = mid+1
    # 만약 과자갯수c가 조카들의 수m보다 적으면
    # mid보다 작은 크기의 과자로 탐색한다
    else:
        end = mid-1
print(ans)