def solution(polynomial):
    answer = ''
    xsum = 0
    nsum = 0
    for p in polynomial.split(' + '):
        if 'x' in p:
            if len(p) == 1:
                xsum += 1
            else:
                xsum += int(p.replace('x', ''))
        else:
            nsum += int(p)

    if xsum > 0 and nsum > 0:
        if xsum == 1:
            answer = 'x + {}'.format(nsum)
        else:
            answer = '{}x + {}'.format(xsum, nsum)

    elif xsum > 0 and nsum == 0:
        if xsum == 1:
            answer = 'x'
        else:
            answer = '{}x'.format(xsum)

    elif nsum > 0 and xsum == 0:
        answer = '{}'.format(nsum)

    print(answer)

    return answer
