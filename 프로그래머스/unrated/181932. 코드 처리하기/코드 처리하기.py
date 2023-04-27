def solution(code):
    answer = 'EMPTY'
    ret = []
    mode = 0
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx%2 == 0:
                    ret.append(code[idx])
            elif code[idx] == '1':
                mode = 1
        
        elif mode == 1:
            if code[idx] != '1':
                if idx%2 == 1:
                    ret.append(code[idx])
            elif code[idx] == '1':
                mode = 0
                
    if len(ret) > 0:
        answer = ''.join(ret)
    return answer