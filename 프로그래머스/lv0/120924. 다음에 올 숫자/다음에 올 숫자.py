def solution(common):
    answer = 0
    
    if common[2] == common[0] + (common[1] - common[0]) * 2: # 1번째 값에 공차*2를 더한 값이 3번째 값이면 등차수열
        answer = common[-1] + (common[1] - common[0])
    else: # 아니면 등비수열
        answer = common[-1] * (common[1] // common[0])
    
    return answer