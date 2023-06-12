def solution(a, b):
    answer = 0
    ab = int(str(a) + str(b))
    ab2 = 2*a*b
    
    answer = ab2 if ab < ab2 else ab
    return answer