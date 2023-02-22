def solution(answers):
    answer = []
    sp1,sp2,sp3 = [1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]
    
    collectCountArr = [0 for _ in range(3)]
    
    for i in range(len(answers)):
        if sp1[i%len(sp1)] == answers[i]:
            collectCountArr[0]+=1
        if sp2[i%len(sp2)] == answers[i]:
            collectCountArr[1]+=1
        if sp3[i%len(sp3)] == answers[i]:
            collectCountArr[2]+=1
            
    maxCollect = max(collectCountArr)
    
    for i in range(3):
        if collectCountArr[i] == maxCollect:
            answer.append(i+1)
            
    return answer