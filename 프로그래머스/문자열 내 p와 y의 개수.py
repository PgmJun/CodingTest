from collections import Counter


def solution(s):
    answer = True
    cnter = Counter(s)

    pcnt = cnter['p'] + cnter['P']
    ycnt = cnter['y'] + cnter['Y']

    if pcnt != ycnt:
        answer = False

    return answer
