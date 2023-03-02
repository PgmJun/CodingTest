import copy


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = copy.deepcopy(array[i-1:j])
        arr.sort()
        answer.append(arr[k-1])

    return answer
