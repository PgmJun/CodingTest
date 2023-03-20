# 아이디 규칙
# 3자 이상 15자 이하
# 알파벳 소문자, 숫자, (- _ .) 만 사용 가능
# 마침표(.)는 처음과 끝에 사용할 수 없음
# 마침표(.)는 연속으로 사용할 수 없음

# 아이디 변경 과정
# 1. 대문자 -> 소문자
# 2. 알파벳 소문자, 숫자, (- _ .) 외에 문자 제거
# 3. 마침표(.)가 연속된 부분을 마침표 하나로 치환
# 4. 마침표가 처음이나 끝에 위치하면 제거
# 5. id가 빈 문자열이 됐다면 "a"로 초기화
# 6. 길이 16자 이상이면 앞선 15문자를 제외하고 모두 제거
# 7. 마지막 문자가 마침표면 제거
# 8. new_id 길이가 2자 이하라면, new_id의 마지막 문자를 new_id 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

def change1(id):
    id = id.lower()
    return id


def change2(id):
    result = []

    for i in range(len(id)):
        nowC = id[i]
        delArr = []
        if nowC.isalpha() or nowC.isdigit() or nowC in ['-', '_', '.']:
            result.append(nowC)
        else:
            continue

    return result


def change3(id):

    for i in range(len(id)+1, 1, -1):
        dots = '.' * i
        if dots in id:
            id = id.replace(dots, '.')

    return id


def change4(id):
    id = list(id)
    for i in [0, -1]:
        if len(id) < 1:
            break
        if id[i] == '.':
            del id[i]

    return id


def change5(id):
    if len(id) == 0:
        id = 'a'

    return id


def change6(id):
    if len(id) > 15:
        id = id[0:15]

    return id


def change7(id):
    if id[-1] == '.':
        id = id[0:-1]

    return id


def change8(id):
    if len(id) < 3:
        c = id[-1]
        while len(id) < 3:
            id += c
    return id


def solution(new_id):
    answer = ''
    new_id = change1(new_id)
    new_id = ''.join(map(str, change2(new_id)))
    new_id = change3(new_id)
    new_id = ''.join(map(str, change4(new_id)))
    new_id = change5(new_id)
    new_id = change6(new_id)
    new_id = change7(new_id)
    new_id = change8(new_id)

    answer = new_id
    return answer
