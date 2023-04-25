def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        
        if flag[i] == True:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        
        elif flag[i] == False:
               answer = answer[0:-arr[i]]
                
        
    return answer