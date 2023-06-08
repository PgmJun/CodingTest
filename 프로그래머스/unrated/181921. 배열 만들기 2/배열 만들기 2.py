def solution(l, r):
    answer = []
    for v in range(l,r+1):
        num = str(v)
        num = num.replace('5','').replace('0','')

        if len(num) == 0:
            answer.append(v)
    if len(answer) == 0:
        answer.append(-1)
    
    return answer