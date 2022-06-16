def solution(p):
    i = 0
    answer = []
    for _ in range(len(p)):
        answer.append(0)

    for i in range(len(p)):
        min = i
        for j in range(i+1,len(p)):
            if p[min] > p[j]:
                min = j
        if i is not min:
            p[min], p[i] = p[i], p[min]
            answer[i]+=1
            answer[min]+=1
    print(answer)
    return answer


solution([2,5,3,1,4])
