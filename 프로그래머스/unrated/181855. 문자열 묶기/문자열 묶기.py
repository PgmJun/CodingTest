def solution(strArr):
    answer = 0
    cntDict = {}
    
    for s in strArr:
        cntDict[len(s)] = 0
    
    for s in strArr:
        cntDict[len(s)] += 1
    
    cntDict = sorted(cntDict.values())
    answer = cntDict[-1]
    
    return answer