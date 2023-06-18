def solution(ingredient):
    answer = 0
    
    stack = ''
    for ingre in ingredient:
        stack += str(ingre)
        if stack[-4:] == '1231':
            stack = stack[0:-4]
            answer+=1

    return answer