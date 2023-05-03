def solution(order):
    AMERICANO = "americano" 
    LATTE = "latte" 
    ANY = "anything"
    
    answer = 0
    for o in order:
        if AMERICANO in o or ANY in o:
            answer += 4500
        elif LATTE in o :
            answer += 5000
        
    return answer