def solution(periods, payments, estimates):
    answer = [0,0]

    for i in range(len(periods)):
        #다음달이 되어도 2년 미만은 VIP가 될 수 없으므로 초반에 필터링
        if (periods[i]+1) < 24:
            continue
        
        #이번달에 VIP가 아닌데 다음달에 VIP가 되는 경우
        #2년이상 5년 미만
        if sum(payments[i]) < 900000 and 60 > periods[i] >= 24 or periods[i]+1 == 24:
            nextSum = sum(payments[i])-payments[i][0]+estimates[i]
            if periods[i]+1 < 60 and nextSum >= 900000:
                answer[0] += 1
            if periods[i]+1 == 60 and nextSum >= 600000:  # 다음달에 5년 이상이 되는 경우
                answer[0] += 1
        #5년 이상
        if sum(payments[i]) < 600000 and periods[i] >= 60:
            nextSum = sum(payments[i])-payments[i][0]+estimates[i]
            if nextSum >= 600000:
                answer[0] += 1

        #이번 달에 VIP인데 다음달에 VIP가 아닌 경우
        #2년이상 5년 미만
        if sum(payments[i]) >= 900000 and 60 > periods[i] >= 24:
            nextSum = sum(payments[i])-payments[i][0]+estimates[i]
            if periods[i]+1 < 60 and nextSum < 900000:
                answer[1]+=1
            if periods[i]+1 == 60 and nextSum < 600000: #다음달에 5년 이상이 되는 경우
                answer[1]+=1
        #5년 이상
        if sum(payments[i]) >= 600000 and periods[i] >= 60:
            nextSum = sum(payments[i])-payments[i][0]+estimates[i]
            if nextSum < 600000:
                answer[1]+=1

        
    return answer


