def solution(arr, divisor):
    answer = []
    
    for v in arr:
        if v % divisor == 0:
            answer.append(v)
            
    answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer