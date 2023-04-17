def solution(quiz):
    answer = []
    for q in quiz:
        v = q.split()
        v1 = int(v[0])
        v2 = int(v[2])
        op = v[1]
                
        ans = 0
        if op == '-':
            ans = v1 - v2
        elif op == '+':
            ans = v1 + v2
        
        if ans == int(v[4]):
            answer.append('O')
        else:
            answer.append('X')
            
    return answer