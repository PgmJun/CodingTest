n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start < end):
    total = 0
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total += x-mid

    # total이 m보다 작다면 적어도 m만큼은 되어야하니까 절단기 높이(mid) 낮추기
    if total < m:
        end = mid-1
    # total이 m보다 크다면 절단기 높이(mid) 높이고 result에 total 삽입
    else:
        result = mid
        start = mid+1

print(result)
