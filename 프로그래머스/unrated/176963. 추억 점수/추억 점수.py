def solution(name, yearning, photo):
    answer = []
    missPoints = {}
    
    for i in range(len(name)):
        missPoints[name[i]] = yearning[i]
    
    
    for p in photo:
        missPoint = 0
        for man in p:
            if man in missPoints.keys():
                missPoint += missPoints[man]
                
        answer.append(missPoint)
    
    return answer