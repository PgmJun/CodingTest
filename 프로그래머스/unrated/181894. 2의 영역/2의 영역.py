def solution(arr):
    answer = []
    if not 2 in arr:
        answer.append(-1)
        return answer
    
    twoIndex = []
    for i in range(len(arr)):
        if arr[i] == 2:
            twoIndex.append(i)
    
    answer = arr[twoIndex[0]:twoIndex[-1]+1]
    return answer