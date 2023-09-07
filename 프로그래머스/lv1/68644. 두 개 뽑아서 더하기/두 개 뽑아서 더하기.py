from itertools import combinations

def solution(numbers):
    answer = []
    
    for a,b in combinations(numbers, 2):
        if (a+b) in answer:
            continue
        answer.append(a+b)
    
    answer.sort()
    
    return answer