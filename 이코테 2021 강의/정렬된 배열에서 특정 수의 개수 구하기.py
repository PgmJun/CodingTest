from bisect import bisect_left, bisect_right


def numCnt():
    # 배열에 찾고자 하는 값이 없다면 None 리턴
    if x not in array:
        return None

    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)

    return right_index-left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

result = numCnt()

if result == None:
    print(-1)
else:
    print(result)
