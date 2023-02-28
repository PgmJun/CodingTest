# record for문으로 순차적으로 조회하면서
    # 명령어가 Change 또는 Enter면 {id : name} 으로 dict에 저장
    # 명령어가 Leave면 continue
    
# 명령어를 (명령어, 아이디) tuple형태로 저장
    
# 저장한 tuple for문으로 순차적 조회하면서
    # 명령어가 Enter면 "dict[id]님이 들어왔습니다."
    # 명령어가 Leave면 "dict[id]님이 나갔습니다."
    # 출력

def solution(record):
    answer = []
    userDict = {}
    commands = []
    
    for command in record:
        # c[0] : 명령 | c[1] : ID | c[2] : 이름
        c = list(command.split())
        if c[0] == 'Enter':
            userDict[c[1]] = c[2]
            commands.append([c[0], c[1]])
        elif c[0] == 'Change':
            userDict[c[1]] = c[2]
        elif c[0] == 'Leave':
            commands.append([c[0], c[1]])
    
    
    for c in commands:
        if c[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(userDict[c[1]]))
        elif c[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(userDict[c[1]]))
    
    return answer