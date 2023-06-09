def solution(picture, k):
    answer = []
    for piece in picture:
        s = ""
        for i in piece:
            s += i*k
        for _ in range(k):
            answer.append(s)
    

    return answer