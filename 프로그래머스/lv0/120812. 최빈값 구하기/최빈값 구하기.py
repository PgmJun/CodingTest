from collections import Counter

def solution(array):
    answer = 0
    
    cnter = Counter(array)
    maxIdx = cnter.most_common(1)[0][0]
    maxCnt = cnter.most_common(1)[0][1]
    
    cnter[maxIdx] = -1
    answer = maxIdx
    
    for key in cnter.keys():
        if cnter[key] == maxCnt:
            answer = -1
            break
        
    return answer