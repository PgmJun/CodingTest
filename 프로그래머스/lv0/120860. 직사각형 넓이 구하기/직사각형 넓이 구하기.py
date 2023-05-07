def solution(dots):
    answer = 0
    distanceA = set()
    distanceB = set()
    
    for dot in dots:
        distanceA.add(dot[0])
    
    for dot in dots:
        distanceB.add(dot[1])
    
    distanceA = list(distanceA)
    distanceB = list(distanceB)
    answer = abs((distanceA[0] - distanceA[1]) * (distanceB[0] - distanceB[1]))
    return answer