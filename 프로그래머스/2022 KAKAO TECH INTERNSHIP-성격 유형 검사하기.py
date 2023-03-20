def solution(survey, choices):
    psnDict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    answer = ''

    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        print(s,c)
        if c == 4: #모르겠음 답변
            continue
        elif c < 4: # 비동의측 답변
            psnDict[s[0]] += 4-c
        elif c > 4: # 동의측 답변
            psnDict[s[1]] += c-4
    
    psnKeys = list(psnDict.keys())
    for i in range(0,len(psnKeys), 2):
        k1,k2 = psnKeys[i], psnKeys[i+1]
        if psnDict[k1] >= psnDict[k2]:
            answer += k1
        else:
            answer += k2
    print(psnDict)
        
    return answer