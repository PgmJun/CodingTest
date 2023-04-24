def makeZero(num):
    cnt = 0
    while num > 1:
        cnt+=1
        if (num % 2) == 0:
            num //= 2
        elif (num % 2) == 1:
            num -= 1
            num //= 2
            
    return cnt
    

def solution(num_list):
    answer = 0
    
    for num in num_list:
        answer += makeZero(num)
        
    return answer