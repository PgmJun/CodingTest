def downCalc(x1, x2):
    if x1 == True or (x1 == False and x2 == True):
        return True
    else:
        return False
    
def upCalc(x1,x2):
    if x1 == True and x2 == True:
        return True
    else:
        return False
    
def solution(x1, x2, x3, x4):
    result1, result2 = downCalc(x1,x2), downCalc(x3,x4)
    answer = upCalc(result1, result2)
    
    return answer