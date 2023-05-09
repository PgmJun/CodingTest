def solution(rank, attendance):
    answer = 0
    result = []
    rankDict = dict()
    
    for i in range(len(rank)):
        if attendance[i]:
            rankDict[rank[i]] = i
    
    rankDict = sorted(rankDict.items())

    for r in rankDict:
        result.append(r[1])
        if len(result) == 3:
            break

    answer = 10000*result[0]+100*result[1]+result[2]
    return answer