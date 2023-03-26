def solution(board, moves):
    answer = 0
    stack = [-1]
    
    for m in moves:
        position = m-1
        
        # 뽑기 기계의 해당 position 맨 아래에 아무것도 없으면 생략
        if board[len(board)-1][position] == 0:
            continue
        
        # 해당 position 맨 위에서 아래로 내려가며 인형 탐색
        for i in range(len(board)):
            doll = board[i][position]
            #인형이 있으면
            if doll != 0:
                # stack 맨위랑 비교해서 같으면 pop()
                if stack[-1] == doll:
                    answer+=2
                    stack.pop()
                # 다르면 append()
                elif stack[-1] != doll:
                    stack.append(doll)
                    
                board[i][position] = 0
                break
            
    return answer