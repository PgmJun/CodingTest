def solution(n, lost, reserve):
    answer = 0
    
    # 학생의 체육복 갯수
    std = [1 for _ in range(n+1)]
    std[0] = 0
    
    for i in range(1,n+1):
        if i in lost: # i번 학생이 잃어버렸으면 
            std[i] -= 1 # i번 학생의 체육복 갯수 -1
        if i in reserve: # i번 학생이 여벌옷이 있다면 
            std[i] += 1 # i번 학생의 체육복 갯수 +1
    
    for i in range(1,n+1):
        if std[i] == 0:
            # 1번 학생일 때 오른쪽만 탐색
            if i == 1:
                if std[i+1] == 2:
                    std[i+1] -= 1
                    std[i] += 1
                    continue
                # 해당 처리가 없으면 중간에 있는 학생일 경우로 조건이 넘어감
                else:
                    continue
            # n번 학생일 때 왼쪽만 탐색
            elif i == n:
                if std[i-1] == 2:
                    std[i-1] -= 1
                    std[i] += 1
                    continue
                # 해당 처리가 없으면 중간에 있는 학생일 경우로 조건이 넘어감
                else:
                    continue
            # 중간에 있는 학생일 때
            if std[i-1] == 2:
                    std[i-1] -= 1
                    std[i] += 1
                    continue
            if std[i+1] == 2:
                    std[i+1] -= 1
                    std[i] += 1
                    continue
    
    for s in std:
        if s != 0:
            answer += 1
    return answer