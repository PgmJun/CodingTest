def solution(num_list):
    answer = 0
    
    multiValue = 1
    for num in num_list:
        multiValue *= num
        
    if multiValue < sum(num_list)**2:
        answer = 1
    
    return answer