def solution(id_pw, db):
    answer = 'fail'
    for data in db:
        if id_pw[0] == data[0]:
            if id_pw[1] == data[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
            break
                
    return answer