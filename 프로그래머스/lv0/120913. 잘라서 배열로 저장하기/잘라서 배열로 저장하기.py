def solution(my_str, n):
    answer = []
    cnt = round(len(my_str) / n)
    
    for i in range(0,len(my_str), n):
        answer.append(my_str[i:i+n])
            
    return answer