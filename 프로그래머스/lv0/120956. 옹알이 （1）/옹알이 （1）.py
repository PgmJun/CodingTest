def solution(babbling):
    canWords = ['aya','ye','woo','ma']
    answer = 0
    
    for b in babbling:
        
        for word in canWords:
            if word in b:
                b = b.replace(word,'_')
        
        b = b.replace('_','')
        if len(b) == 0:
            answer += 1
            
    return answer