def solution(array):
    answer = 0
    
    for v in array:
        answer += str(v).count('7')
    return answer